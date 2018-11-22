# Kafka小组作业

## 集群搭建

### 机器资源

- 系统
    1. CentOS
- 网络
    1. 有内部DNS服务或者修改hosts文件保证集群机器通过hostname相连。
    2. 修改防火墙，暴露相关端口。（2181，9092等）
- 磁盘
    1. 因为linux的磁盘是通过挂载点加入整个文件系统的，不能想当然认为某个目录下就具有足够大的磁盘空间，需要确认好文件存放目录，保证空间足够。

### 安装文件

- JDK 1.8
- Zookeeper 3.4.x
- kafka 2.0.0

### 运行

- Zookeeper不同节点的配置文件没有区别，这使得启动较为容易，先copy一份配置到本地，修改后scp到集群机器上。
- kafka的配置文件中需要指明id，这里我同样copy一份配置，上传配置，然后通过sed修改broker_id。
- 在远程写shell脚本调用时，经常需要考虑加\，比如\\$，根据语义不同：本机解析和远程解析。
- shell的缩进没什么意义，但可读性好，只是cat >> eof …… eof的写法，会把空格制表都算上。
- 一些命令会有交互过程，差不多就是-y -i -f等就可以去掉交互。

## 集群测试

### kafka常用配置

- broker
  - 内存分配默认只有1g，最好增大至6g，缓冲buffer不宜过大，不然会出现阻塞，程序假死。
- topic
  - partition才具有master/slave，所以分区不能太少，应该和节点数相当或者稍多。
  - replicafactor，备份数量，一般为3。
- producer
  - acks：决定broker返回的时间点，0: 一接收就返回 1: 一个broker持久化返回 2: 所有副本持久化返回
- consumer
  - consumer具有client-id和group-id，以此来区分它的offset。

### 测试工具

- tsung
- jmeter
  - 优势在是java编写的，开发插件相对容易。（有个pepperbox可以发起kafka请求)

### 测试数据

- 机器性能
  - 网络：万兆网卡
  - 磁盘：写 240MB/s，读 374~400MB/s。
    ``` shell
    sync; time dd if=/dev/zero of=/test.dbf bs=8k count=300000
    记录了300000+0 的读入
    记录了300000+0 的写出
    2457600000字节(2.5 GB)已复制，10.1918 秒，241 MB/秒
    hdparm -Tt /dev/sda
    /dev/sda:
    Timing cached reads:   20540 MB in  2.00 seconds = 10283.29 MB/sec
    Timing buffered disk reads: 1124 MB in  3.00 seconds = 374.08 MB/sec
    ```
- bench测试
  - bin/kafka-consumer-perf-test.sh --broker-list localhost:9092 --consumer.config config/consumer.properties --num-fetch-threads 20 --topic test2 --messages 2000000
  - data.consumed.in.MB, MB.sec, data.consumed.in.nMsg, nMsg.sec, rebalance.time.ms, fetch.time.ms, fetch.MB.sec, fetch.nMsg.sec
  - 416.7174, 14.6561, 1243301, 43727.3942, 53, 28380, 14.6835, 43809.0557
  - 大约每秒四万条读取，14MB数据，主要是由于单条数据较小，并且测试能力弱，所以数据量上不去。

- jmeter测试
  - jmter-producer测试，5000数量的线程池，单条消息大约5000byte。
  - 测试机输出在600MB/s，每秒120000条数据。
  - 三节点集群，各自输入在200MB/s，同时进行100MB/s的数据同步。
  - 由于超出了磁盘写的能力，这里ISR副本会落后，导致停止测试后，还会进行一段时间的同步。

### 性能监控

- prometheus

### 集群监控

- cruise-control
  - 支持2.0.0版本，但没有图形化
- kafka-manager
  - 有图形化，但没有跟上最新版本，虽然勉强也能用，但可能有未知bug。

## 多数据中心

多数据中心对于大公司而言也是必然场景，此时就存在多集群的备份，同步等问题，非常麻烦。

- uReplicator：Uber开发的一个mirrormaker的增强版，用于跨集群拷贝数据。
- confluent replicator connector： Confluent开发的一种connector，也用于跨集群拷贝。 
