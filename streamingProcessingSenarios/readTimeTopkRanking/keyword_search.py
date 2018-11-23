from kafka import KafkaProducer
import json
import random


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=[
        '212.64.16.70:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
    for i in range(500):
        keyword = random.randint(0, 90)

        jsonObj = {}
        jsonObj["goodID"] = keyword
        future = producer.send(
            'topK', jsonObj, partition=0)
        result = future.get(timeout=10)
