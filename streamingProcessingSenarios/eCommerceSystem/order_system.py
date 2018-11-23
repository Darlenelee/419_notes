from kafka import KafkaProducer
import json
import random


def fake_add_order_to_database(goodID, number, userID):
    pass

def receive_new_order(goodID, number, userID):
    # Order system(Client of Kafka) receives a new order from a customer.
    fake_add_order_to_database(goodID, number, userID)


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=[
        '212.64.16.70:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
    for i in range(100):
        goodID = random.randint(0, 100000)
        number = random.randint(0, 100000)
        userID = random.randint(0, 100000)

        receive_new_order(goodID, number, userID)

        jsonObj = {}
        jsonObj["goodID"] = goodID
        jsonObj["number"] = number
        jsonObj["userID"] = userID

        future = producer.send(
            'newOrder', jsonObj , partition=0)
        result = future.get(timeout=10)
        print(result)
