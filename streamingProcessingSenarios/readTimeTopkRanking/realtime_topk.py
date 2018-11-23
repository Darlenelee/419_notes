from kafka import KafkaConsumer
import json
import random

if __name__ == "__main__":
    count = {}
    maxKeyword = ""
    #Here 
    consumer = KafkaConsumer('topK', group_id='group2',
                             bootstrap_servers=['212.64.16.70:9092'])
    for msg in consumer:
        values = msg.value
        try:
            count[values["goodID"]] = count[values["goodID"]] + 1
        except KeyError:
            count[values["goodID"]] = 1
        
        if len(maxKeyword) == 0:
            maxKeyword = values["goodID"]
        else:
            if(count[values["goodID"]] > count[maxKeyword]):
                maxKeyword = values["goodID"]
        print("Read Time Top1: ", values["goodID"])
