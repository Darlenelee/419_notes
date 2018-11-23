from kafka import KafkaConsumer


def fake_write_inventory_database(msg):
    # write the data to Database
    pass


def fake_process_new_order(msg):
    # Inventory system(Client of Kafka) receives a new message.
    fake_write_inventory_database(msg)


if __name__ == "__main__":
    consumer = KafkaConsumer('newOrder', group_id='group2',
                             bootstrap_servers=['212.64.16.70:9092'])
    for msg in consumer:
        fake_process_new_order(msg)
