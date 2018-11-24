from kafka import KafkaProducer
 import json
 import random
 producer = KafkaProducer(bootstrap_servers=['212.64.16.70:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
 for i in range(100):
     high=random.randint(20,30)
     low=random.randint(10,20)
     future = producer.send('temperature' ,  value= {'high' : str(high),'low':str(low)}, partition= 0)
     result = future.get(timeout= 10)
     print(result) 