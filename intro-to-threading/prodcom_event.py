#!/usr/bin/env python3
import concurrent.futures
import logging
import random
import threading
import time


class Pipeline:
    """Class to allow a single element pipeline between producer and consumer.
    """

    def __init__(self):
        self.value = 0
        self._set_lock = threading.Lock()
        self._get_lock = threading.Lock()
        self._get_lock.acquire()

    def get_value(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self._get_lock.acquire()
        logging.debug("%s:have getlock", name)
        value = self.value
        logging.debug("%s:about to release setlock", name)
        self._set_lock.release()
        logging.debug("%s:setlock released", name)
        return value

    def set_value(self, value, name):
        logging.debug("%s:about to acquire setlock", name)
        self._set_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.value = value
        logging.debug("%s:about to release getlock", name)
        self._get_lock.release()
        logging.debug("%s:getlock released", name)


def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        new_datapoint = random.randint(1, 101)
        # Sleep to simulate waiting for data from network
        # time.sleep(float(new_datapoint)/100)
        logging.info("Producer got data %d", new_datapoint)
        pipeline.set_value(new_datapoint, "Producer")
        if event.is_set():
            logging.info("Producer received internal event. Exiting")

        # don't put sleep here as this will cause the system to stall when the
        # consumer is active.  That will result in deadlock.
        # time.sleep(float(new_datapoint)/100)

    logging.info("Producer received event. Exiting")


def consumer(pipeline, event):
    """ Pretend we're saving a number in the database. """
    datapoint = 0
    while not event.is_set():
        datapoint = pipeline.get_value("Consumer")
        logging.info("Consumer storing data: %d", datapoint)

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
