# consumer.py

from kafka3 import KafkaConsumer

consumer = KafkaConsumer("datascience")
for record in consumer:
    message = record.value.decode("utf-8")
    print(f"Got message: {message}")
