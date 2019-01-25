#!/usr/bin/env python3
import concurrent.futures
import logging
import queue
import random
import threading
import time

SENTINEL = -1

class Pipeline():
    '''Class to allow a single element pipeline between producer and consumer.
    '''
    def __init__(self):
        self.Q = queue.Queue(maxsize=10)

    def empty(self):
        return self.Q.empty()

    def size(self):
        return self.Q.qsize()

    def get_value(self, name):
        logging.debug(f"{name}:about to get from queue")
        value = self.Q.get()
        logging.debug(f"{name}:got {value} from queue")
        return value

    def set_value(self, value, name):
        logging.debug(f"{name}:about to add {value} to queue")
        self.Q.put(value)
        logging.debug(f"{name}:added {value} to queue")


def producer(pipeline, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        new_datapoint = random.randint(1,101)
        # Sleep to simulate waiting for data from network
        # time.sleep(float(new_datapoint)/100)
        logging.warning(f"Producer got data {new_datapoint}")
        pipeline.set_value(new_datapoint, "Producer")

    logging.warning(f"Producer received event. Exiting")

def consumer(pipeline, event):
    ''' Pretend we're saving a number in the database. '''
    while not event.is_set() or not pipeline.empty():
        datapoint = pipeline.get_value("Consumer")
        logging.warning(f"Consumer storing data: {datapoint}" +
                        f" (size={pipeline.size()})")

    logging.warning(f"Consumer received event. Exiting")


if __name__ == "__main__":
    # FORMAT = '%(asctime)-15s %(message)s'
    FORMAT = '%(message)s'
    logging.basicConfig(format=FORMAT)
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(1)
        logging.warning("Main: about to set event")
        event.set()


