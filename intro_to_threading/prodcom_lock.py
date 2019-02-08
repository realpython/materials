#!/usr/bin/env python3
import concurrent.futures
import logging
import random
import threading
import time

SENTINEL = -1

class Pipeline():
    '''Class to allow a single element pipeline between producer and consumer.
    '''
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.comsumer_lock = threading.Lock()
        self.comsumer_lock.acquire()

    def get_message(self, name):
        logging.debug(f"{name}:about to acquire getlock")
        self.comsumer_lock.acquire()
        logging.debug(f"{name}:have getlock")
        message = self.message
        logging.debug(f"{name}:about to release setlock")
        self.producer_lock.release()
        logging.debug(f"{name}:setlock released")
        return message

    def set_message(self, message, name):
        logging.debug(f"{name}:about to acquire setlock")
        self.producer_lock.acquire()
        logging.debug(f"{name}:have setlock")
        self.message = message
        logging.debug(f"{name}:about to release getlock")
        self.comsumer_lock.release()
        logging.debug(f"{name}:getlock released")



def producer(pipeline):
    '''Pretend we're getting a message from the network.'''
    for index in range(10):
        message = random.randint(1,101)
        logging.warning(f"Producer got message: {message}")
        pipeline.set_message(message, "Producer")

    # send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")

def consumer(pipeline):
    ''' Pretend we're saving a number in the database. '''
    message = 0
    while message != SENTINEL:
        message = pipeline.get_message("Consumer")
        if message != SENTINEL:
            logging.warning(f"Consumer storing message: {message}")

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')
    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
