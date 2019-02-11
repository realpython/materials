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
        logging.debug("%s:about to get from queue", name)
        value = self.Q.get()
        logging.debug("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        logging.debug("%s:about to add %d to queue", name, value)
        self.Q.put(value)
        logging.debug("%s:added %d to queue", name, value)


def producer(pipeline, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    ''' Pretend we're saving a number in the database. '''
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info("Consumer storing message: %s  (queue size=%s)", message,
                     pipeline.size())

    logging.info("Consumer received EXIT event. Exiting")


if __name__ == "__main__":
    format='%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    # logging.basicConfig(format=format, level=logging.DEBUG, datefmt='%H:%M:%S')

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
