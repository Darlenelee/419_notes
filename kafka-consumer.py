from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', group_id= 'group2', bootstrap_servers= ['212.64.16.70:9092'])
for msg in consumer:
    print(msg)