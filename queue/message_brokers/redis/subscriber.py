# subscriber.py

import redis

with redis.Redis() as client:
    pubsub = client.pubsub()
    pubsub.subscribe("chatroom")
    for message in pubsub.listen():
        if message["type"] == "message":
            body = message["data"].decode("utf-8")
            print(f"Got message: {body}")
