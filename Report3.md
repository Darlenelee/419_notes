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

---
# Stream Computing framework Report —— Storm & Spark

---

## Storm

### Storm简介

Storm是Twitter开源的分布式实时大数据处理框架，最早开源于github，从0.9.1版本之后，归于Apache社区，被业界称为实时版Hadoop。随着越来越多的场景对Hadoop的MapReduce高延迟无法容忍，比如网站统计、推荐系统、预警系统、金融系统(高频交易、股票)等等，大数据实时处理解决方案（流计算）的应用日趋广泛，目前已是分布式技术领域最新爆发点，而Storm更是流计算技术中的佼佼者和主流。

Storm的集群表面上看和hadoop的集群非常像。但是在Hadoop上面你运行的是MapReduce的Job, 而在Storm上面你运行的是Topology。它们是非常不一样的 — 一个关键的区别是： 一个MapReduce Job最终会结束， 而一个Topology运永远运行（除非你显式的杀掉他）。

在Storm的集群里面有两种节点： 控制节点(master node)和工作节点(worker node)。控制节点上面运行一个后台程序：Nimbus， 它的作用类似Hadoop里面的JobTracker。Nimbus负责在集群里面分布代码，分配工作给机器， 并且监控状态。
每一个工作节点上面运行一个叫做Supervisor的节点（类似 TaskTracker）。Supervisor会监听分配给它那台机器的工作，根据需要 启动/关闭工作进程。每一个工作进程执行一个Topology（类似 Job）的一个子集；一个运行的Topology由运行在很多机器上的很多工作进程 Worker（类似 Child）组成。

以下是Storm与hadoop的升级版本Spark的对比。

|  对比点    |  Storm | Spark Streaming | 
| :---------: | :----------: | :---: | 
| 实时计算模型 | 纯实时，来一条数据，处理一条数据 | 准实时，对一个时间段内的数据收集起来，作为一个RDD，再处理 |
| 实时计算延迟度 | 毫秒级| 秒级 |
| 事务机制 | 支持完善 | 支持，但不够完善 |
| 健壮性 / 容错性 | ZooKeeper，Acker，非常强 | Checkpoint，WAL，一般|
| 动态调整并行度 | 支持 | 不支持 |


### Storm角色

主节点：Nimbus

从节点：Supervisor

### Storm基本概念

Nimbus：主节点

Supervisor：从节点

Worker：任务工作进程，类似于YARN的ApplicationMaster，可以存在多个，不同的任务有不同的Worker

Executor：Worker进程在执行任务时，会启动多个Executor现成

Stream：Stream是storm里面的关键抽象。一个stream是一个没有边界的tuple序列。

Spout：抽取数据并将数据进行分发的阶段

Bolt：将分发的数据进行具体操作的阶段

Topology：task任务的拓扑结构，是一个DAG有向无环图
解释：为了在storm上面做实时计算， 你要去建立一些topologies。一个topology就是一个计算节点所组成的图。Topology里面的每个处理节点都包含处理逻辑， 而节点之间的连接则表示数据流动的方向。

Stream/Spout/Bolt/Topology详细解释：

storm提供一些原语来分布式地、可靠地把一个stream传输进一个新的stream。比如： 你可以把一个tweets流传输到热门话题的流。
storm提供的最基本的处理stream的原语是spout和bolt。你可以实现Spout和Bolt对应的接口以处理你的应用的逻辑。
spout的流的源头。比如一个spout可能从Kestrel队列里面读取消息并且把这些消息发射成一个流。又比如一个spout可以调用twitter的一个api并且把返回的tweets发射成一个流。
通常Spout会从外部数据源（队列、数据库等）读取数据，然后封装成Tuple形式，之后发送到Stream中。Spout是一个主动的角色，在接口内部有个nextTuple函数，Storm框架会不停的调用该函数。

![此处输入图片的描述][1]

bolt可以接收任意多个输入stream， 作一些处理， 有些bolt可能还会发射一些新的stream。一些复杂的流转换， 比如从一些tweet里面计算出热门话题， 需要多个步骤， 从而也就需要多个bolt。 Bolt可以做任何事情: 运行函数， 过滤tuple, 做一些聚合， 做一些合并以及访问数据库等等。
Bolt处理输入的Stream，并产生新的输出Stream。Bolt可以执行过滤、函数操作、Join、操作数据库等任何操作。Bolt是一个被动的 角色，其接口中有一个execute(Tuple input)方法，在接收到消息之后会调用此函数，用户可以在此方法中执行自己的处理逻辑。

![此处输入图片的描述][2]

spout和bolt所组成一个网络会被打包成topology， topology是storm里面最高一级的抽象（类似 Job）， 你可以把topology提交给storm的集群来运行。topology的结构在Topology那一段已经说过了，这里就不再赘述了。

![此处输入图片的描述][3]
topology结构

topology里面的每一个节点都是并行运行的。 在你的topology里面， 你可以指定每个节点的并行度， storm则会在集群里面分配那么多线程来同时计算。
一个topology会一直运行直到你显式停止它。storm自动重新分配一些运行失败的任务， 并且storm保证你不会有数据丢失， 即使在一些机器意外停机并且消息被丢掉的情况下。

### Storm 工作机制

下图是Topology的提交流程图。

![此处输入图片的描述][4]

下图是Storm的数据交互图。可以看出两个模块Nimbus和Supervisor之间没有直接交互。状态都是保存在Zookeeper上。Worker之间通过ZeroMQ传送数据。
![此处输入图片的描述][5]

###Storm集群运行机制

主节点Nimbus

管理所有从节点supervisor，当主节点nimbus启动后会定时向zookeeper集群发送自己的当前状态信息，同时也可以获取所有从节点Supervisor的状态信息

从节点Supervisor

定时向zookeeper集群汇报自己的状态信息，同时接受主节点Nimbus派发过来的任务。

Zookeeper的作用

Storm的所有节点的状态信息都保存在zookeeper当中，如果有某个节点挂掉了，只需要启动一个新的节点来替代即可，新的节点启动后，会自动从zookeeper中读取之前的状态信息，然后恢复到该状态下。同时也不必担心task任务意外终止，因为可以通过zookeeper来恢复该任务，也就是重启挂掉的task。nimbus和supervisor之间的状态同步全部依赖zookeeper来实现


### Storm集群配置

Storm集群配置结构如下图所示。

![此处输入图片的描述][6]


 参考资料：
 http://www.cnblogs.com/wuxiang/p/5629138.html
 https://www.jianshu.com/p/7e5fc624861b
 https://blog.csdn.net/u013384984/article/details/79415003


  [1]: http://www.aboutyun.com/data/attachment/forum/201404/15/225642avl8cwe7bw9nc8fm.jpg
  [2]: http://www.aboutyun.com/data/attachment/forum/201404/15/225643wq3b3babkpeqh5z5.jpg
  [3]: http://www.aboutyun.com/data/attachment/forum/201404/15/225643pjbhjccbkt94cmst.png
  [4]: http://jbcdn2.b0.upaiyun.com/2013/09/topology021.jpg
  [5]: http://jbcdn2.b0.upaiyun.com/2013/09/topology03.png
  [6]: http://www.aboutyun.com/data/attachment/forum/201404/15/225641mt3v1okkkrkkp3rk.jpg
