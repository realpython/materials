#!/usr/bin/env python3
import concurrent.futures
import logging
import queue
import random
import threading
import time

class Pipeline():
    def __init__(self):
        self.Q = queue.Queue(maxsize=10)

    def empty(self):
        return self.Q.empty()

    def size(self):
        return self.Q.qsize()

    def get_message(self, name):
        logging.debug(f"{name}:about to get from queue")
        value = self.Q.get()
        logging.debug(f"{name}:got {value} from queue")
        return value

    def set_message(self, value, name):
        logging.debug(f"{name}:about to add {value} to queue")
        self.Q.put(value)
        logging.debug(f"{name}:added {value} to queue")


def producer(pipeline, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        message = random.randint(1,101)
        logging.warning(f"Producer got message: {message}")
        pipeline.set_message(message, "Producer")

    logging.warning(f"Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    ''' Pretend we're saving a number in the database. '''
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.warning(f"Consumer storing message: {message}" +
                        f" (queue size={pipeline.size()})")

    logging.warning(f"Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.warning("Main: about to set event")
        event.set()
