import logging
import random
import threading
import time
from collections import deque

logging.basicConfig(level=logging.INFO, format="%(message)s")


def _wait_seconds(mins, maxs):
    time.sleep(mins + random.random() * (maxs - mins))


def produce(queue, size):
    while True:
        if len(queue) < size:
            value = random.randint(0, 9)
            queue.append(value)
            logging.info("Produced: %d -> %s", value, str(queue))
        else:
            logging.info("Queue is saturated")
        _wait_seconds(0.1, 0.5)


def consume(queue):
    while True:
        try:
            value = queue.popleft()
        except IndexError:
            logging.info("Queue is empty")
        else:
            logging.info("Consumed: %d -> %s", value, str(queue))
        _wait_seconds(0.2, 0.7)


logging.info("Starting Threads...\n")
logging.info("Press Ctrl+C to interrupt the execution\n")

shared_queue = deque()

threading.Thread(target=produce, args=(shared_queue, 10)).start()
threading.Thread(target=consume, args=(shared_queue,)).start()
