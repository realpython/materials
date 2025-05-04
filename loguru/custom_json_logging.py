import json

from loguru import logger


def simple_serializer(record):
    subset = {
        "time": record["time"].timestamp(),
        "level": record["level"].name,
        "message": record["message"],
        "context": record["extra"],  # Include any bound context
    }
    return json.dumps(subset)


def add_serialization(record):
    record["extra"]["json_output"] = simple_serializer(record)


logger.remove()
logger = logger.patch(add_serialization)
logger.add("custom.json", format="{extra[json_output]}")
logger.bind(user="john").info("User logged in")
logger.bind(order_id=12345).info("Order processed")
