## Kafka trial with python clients

使用场景：天气信息，可以根据温度生成相应的提示。生产者和消费者通过卡夫卡客户端异步发送和接受100条json信息，其中每个json里面有一个high一个low信息。

### Producer

1. 先KafkaProducer建立连接
2. 使用一个for循环
3. 每个循环内生成两个随机数（10到20和20到30各一个）作为模拟温度数据
4. dump成json发送



