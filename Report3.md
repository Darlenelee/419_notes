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
## 设计流处理的使用场景
    代码在[streamingProcessingSenarios]目录下
### 1. 流处理在实时关键字热度排名中的应用
在系统中，我们经常会遇到这样的需求：将大量（比如几十万、甚至上百万）的对象进行排序，然后只需要取出最Top的前N名作为排行榜的数据，这即是一个TopN算法。但在刘流处理的模式下，我们：
- 需要实时评估当前的TopN items. 其中的items可以是关键字、商品等。
- 算法有原来的统一进行大规模数据排序变成了流处理在线处理模式。

### 2. 流处理在常见电商交易系统中的应用
考虑最典型的电商交易系统。用户下单之后，订单系统需要通知库存系统。传统的做法是，订单系统调用库存系统的接口。在这种模式下，最主要的确缺点有：
- 假如库存系统无法访问，则订单减库存将失败，从而导致订单失败
- 订单系统与库存系统耦合

如何解决以上问题呢？引入应用流处理的方案之后：
- 订单系统：用户下单后，订单系统完成持久化处理，将消息写入消息队列，返回用户订单下单成功
- 库存系统：订阅下单的消息，采用拉/推的方式，获取下单信息，库存系统根据下单信息，进行库存操作


这样做的优点是：
- 假如：在下单时库存系统不能正常使用。也不影响正常下单，因为下单后，订单系统写入消息队列就不再关心其他的后续操作了。实现订单系统与库存系统的应用解耦

## Stream Computing framework Report —— Storm & Spark

### Storm

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

### Storm基本概念

- Nimbus：主节点

- Supervisor：从节点

- Worker：任务工作进程，类似于YARN的ApplicationMaster，可以存在多个，不同的任务有不同的Worker

- Executor：Worker进程在执行任务时，会启动多个Executor现成

- Stream：Stream是storm里面的关键抽象。一个stream是一个没有边界的tuple序列。

- Spout：抽取数据并将数据进行分发的阶段

- Bolt：将分发的数据进行具体操作的阶段

- Topology：task任务的拓扑结构，是一个DAG有向无环图
    解释：为了在storm上面做实时计算， 你要去建立一些topologies。一个topology就是一个计算节点所组成的图。Topology里面的每个处理节点都包含处理逻辑， 而节点之间的连接则表示数据流动的方向。

- Stream/Spout/Bolt/Topology详细解释：

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

### Storm集群运行机制

- 主节点Nimbus

管理所有从节点supervisor，当主节点nimbus启动后会定时向zookeeper集群发送自己的当前状态信息，同时也可以获取所有从节点Supervisor的状态信息

- 从节点Supervisor

定时向zookeeper集群汇报自己的状态信息，同时接受主节点Nimbus派发过来的任务。

- Zookeeper的作用

Storm的所有节点的状态信息都保存在zookeeper当中，如果有某个节点挂掉了，只需要启动一个新的节点来替代即可，新的节点启动后，会自动从zookeeper中读取之前的状态信息，然后恢复到该状态下。同时也不必担心task任务意外终止，因为可以通过zookeeper来恢复该任务，也就是重启挂掉的task。nimbus和supervisor之间的状态同步全部依赖zookeeper来实现


### Storm集群配置

Storm集群配置结构如下图所示。

![此处输入图片的描述][6]

### spark
### 简介
Apache Spark是专为大规模数据处理而设计的快速通用的计算引擎。Spark是UC Berkeley AMP lab (加州大学伯克利分校的AMP实验室)所开源的类Hadoop MapReduce的通用并行框架。Spark是一个用来实现快速而通用的集群计算的平台。扩展了广泛使用的MapReduce计算模型，而且高效地支持更多的计算模式，包括交互式查询和流处理。在处理大规模数据集的时候，速度是非常重要的。Spark的一个重要特点就是能够在内存中计算，因而更快。即使在磁盘上进行的复杂计算，Spark依然比MapReduce更加高效。
### 基本概念与原理
一个完整的Spark应用程序在提交集群运行时，涉及到如下图所示的组件：

![spark应用程序示意图](https://img-blog.csdn.net/20150920083018462)

各Spark应用程序以相互独立的进程集合运行于集群之上，由SparkContext对象进行协调。SparkContext对象可以视为Spark应用程序的入口，被称为driver program。SparkContext可以与不同种类的集群资源管理器(Cluster Manager），例如Hadoop Yarn、Mesos等进行通信，从而分配到程序运行所需的资源。获取到集群运行所需的资源后，SparkContext将得到集群中其它工作节点（Worker Node） 上对应的Executors （不同的Spark应用程序有不同的Executor，它们之间也是独立的进程，Executor为应用程序提供分布式计算及数据存储功能）。之后SparkContext将应用程序代码分发到各Executors，最后将任务（Task）分配给executors执行。

- Application（Spark应用程序）：运行于Spark上的用户程序，由集群上的一个driver program（包含SparkContext对象）和多个executor线程组成
- Application jar（Spark应用程序JAR包）：包含用户Spark应用程序的jar包
- Driver program：包含main方法的程序，负责创建SparkContext对象
- Cluster manager：集群资源管理器，例如Mesos，Hadoop Yarn
- Deploy mode：部署模式，用于区别driver program的运行方式
    - 集群模式(cluter mode)，driver在集群内部启动
    - 客户端模式（client mode），driver进程从集群外部启动
- Worker node：工作节点，集群中可以运行Spark应用程序的节点
- Executor：Worker node上的进程，该进程用于执行具体的Spark应用程序任务，负责任务间的数据维护（数据在内存中或磁盘上)。不同的Spark应用程序有不同的Executor
- Task：运行于Executor中的任务单元，Spark应用程序最终被划分为经过优化后的多个任务的集合
- Job：由多个任务构建的并行计算任务，具体为Spark中的action操作，如collect,save等
- Stage：每个job将被拆分为更小的task集合，这些任务集合被称为stage，各stage相互独立（类似于MapReduce中的map stage和reduce stage），由于它由多个task集合构成，因此也称为TaskSet
### Spark RDD
RDD是Spark的基本抽象，是一个弹性分布式数据集，代表着不可变的，分区（partition）的集合，能够进行并行计算。也即是说它是一系列的分片、比如说128M一片，类似于Hadoop的split；在每个分片上都有一个函数去执行/迭代/计算它。它也是一系列的依赖，比如RDD1转换为RDD2，RDD2转换为RDD3，那么RDD2依赖于RDD1，RDD3依赖于RDD2。对于一个Key-Value形式的RDD，可以指定一个partitioner，告诉它如何分片，常用的有hash、range。
### Spark Streaming
Streaming是一种数据传送技术，它把客户机收到的数据变成一个稳定连续的流，源源不断的送出，使用户听到的声音或者看到的图像十分平稳，而且用户在整个文件传送完之前就可以开始浏览文件。 
Spark Streaming是构建在Spark上处理Stream数据的框架，具有可扩展，高吞吐、容错性强的特点，它从数据源（soket、flume、kafka）得到数据，并将流式数据分成很多RDD，根据时间间隔以批次（batch）为单位进行处理，能实现实时统计，累加，和一段时间内的指标的统计。
- 当运行Spark Streaming 框架时，Application会执行StreamingContext，并且在底层运行的是SparkContext，然后Driver在每个Executor上一直运行一个Receiver来接受数据
![spark streaming示意图1](http://static.zybuluo.com/vin123456/2gxlc1ffqvjqedp8vxp7nqr9/image_1as49tnf31qq5vet2gu1bs41ivdcs.png)
- Receiver通过input stream接收数据并将数据分成块（blocks），之后存储在Executor的内存中，blocks会在其他的Executor上进行备份
![spark streaming示意图1](http://static.zybuluo.com/vin123456/3w52offyj0bajrvia7m4mwra/image_1as4a2m8a18obaub100k1koh1g7nd9.png)
- Executor将存储的blocks回馈给StreamingContext，当经过一定时间后，StreamingContext将在这一段时间内的blocks，也称为批次（batch）当作RDD来进行处理，并通过SparkContext运行Spark jobs，Spark jobs通过运行tasks在每个Executor上处理存储在内存中的blocks
![spark streaming示意图1](http://static.zybuluo.com/vin123456/zut3psn48e4oy0trxf1dd73k/image_1as4aa2dt14n25641b50e731ubldm.png)
- 这个循环每隔一个批次执行一次
![spark streaming示意图1](http://static.zybuluo.com/vin123456/3pxiemu9zh482xxlha1u5z2n/image_1as4acn181ais15h412il7i2cjbe3.png)
### 运行模式
目前最为常用的Spark运行模式有：
- local：本地线程方式运行，主要用于开发调试Spark应用程序
- Standalone：利用Spark自带的资源管理与调度器运行Spark集群，采用Master/Slave结构，为解决单点故障，可以采用ZooKeeper实现高可靠（High Availability，HA）
- Apache Mesos ：运行在著名的Mesos资源管理框架基础之上，该集群运行模式将资源管理交给Mesos，Spark只负责进行任务调度和计算
- Hadoop YARN : 集群运行在Yarn资源管理器上，资源管理交给Yarn，Spark只负责进行任务调度和计算。这是最为常用的运行模式。
### 优点
- 性能：内存计算下，Spark 比 Hadoop 快100倍，且Spark支持交互式计算与各种复杂算法。
- 易用性：Spark提供了80多个高级运算符。同时Spark的API可以将集群管理和计算任务解耦，使开发者可以专注于计算。
- 通用性：Spark提供了大量的库，包括SQL、DataFrames、MLlib、GraphX、Spark Streaming，开发者可以在同一个应用程序中组合使用这些库。Spark可以用于各种应用场景，例如SQL查询、文本处理、机器学习等。
- 支持多种资源管理器：Spark 支持 Hadoop YARN，Apache Mesos，及其自带的独立集群管理器
### 参考资料
[百度百科-spark](https://baike.baidu.com/item/SPARK/2229312?fr=aladdin)

[Spark修炼之道（进阶篇）——Spark入门到精通：第四节 Spark编程模型（一)](https://blog.csdn.net/lovehuangjiaju/article/details/48580863)

[Spark基础全解析](https://blog.csdn.net/vinfly_li/article/details/79396821#spark-streaming)

 http://www.cnblogs.com/wuxiang/p/5629138.html

 https://www.jianshu.com/p/7e5fc624861b
 
 https://blog.csdn.net/u013384984/article/details/79415003


  [1]: http://www.aboutyun.com/data/attachment/forum/201404/15/225642avl8cwe7bw9nc8fm.jpg
  [2]: http://www.aboutyun.com/data/attachment/forum/201404/15/225643wq3b3babkpeqh5z5.jpg
  [3]: http://www.aboutyun.com/data/attachment/forum/201404/15/225643pjbhjccbkt94cmst.png
  [4]: http://jbcdn2.b0.upaiyun.com/2013/09/topology021.jpg
  [5]: http://jbcdn2.b0.upaiyun.com/2013/09/topology03.png
  [6]: http://www.aboutyun.com/data/attachment/forum/201404/15/225641mt3v1okkkrkkp3rk.jpg
