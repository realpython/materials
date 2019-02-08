#!/usr/bin/env python3
import concurrent.futures
import logging
import random
import threading
import time


class Pipeline():
    '''Class to allow a single element pipeline between producer and consumer.
    '''
    def __init__(self):
        self.value = 0
        self._set_lock = threading.Lock()
        self._get_lock = threading.Lock()
        self._get_lock.acquire()

    def get_value(self, name):
        logging.debug(f"{name}:about to acquire getlock")
        self._get_lock.acquire()
        logging.debug(f"{name}:have getlock")
        value = self.value
        logging.debug(f"{name}:about to release setlock")
        self._set_lock.release()
        logging.debug(f"{name}:setlock released")
        return value

    def set_value(self, value, name):
        logging.debug(f"{name}:about to acquire setlock")
        self._set_lock.acquire()
        logging.debug(f"{name}:have setlock")
        self.value = value
        logging.debug(f"{name}:about to release getlock")
        self._get_lock.release()
        logging.debug(f"{name}:getlock released")

def producer(pipeline, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        new_datapoint = random.randint(1,101)
        # Sleep to simulate waiting for data from network
        # time.sleep(float(new_datapoint)/100)
        logging.warning(f"Producer got data {new_datapoint}")
        pipeline.set_value(new_datapoint, "Producer")
        if event.is_set():
            logging.warning(f"Producer received internal event. Exiting")

        # don't put sleep here as this will cause the system to stall when the
        # consumer is active.  That will result in deadlock.
        # time.sleep(float(new_datapoint)/100)

    logging.warning(f"Producer received event. Exiting")


def consumer(pipeline, event):
    ''' Pretend we're saving a number in the database. '''
    datapoint = 0
    while not event.is_set():
        datapoint = pipeline.get_value("Consumer")
        logging.warning(f"Consumer storing data: {datapoint}")

    logging.warning(f"Consumer received event. Exiting")


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
