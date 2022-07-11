# producer.py

from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(topic="datascience", value=message.encode("utf-8"))
