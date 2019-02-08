#!/usr/bin/env python3
import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(queue, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        message = random.randint(1,101)
        logging.warning(f"Producer got message: {message}")
        queue.put(message)

    logging.warning(f"Producer received event. Exiting")

def consumer(queue, event):
    ''' Pretend we're saving a number in the database. '''
    while not event.is_set() or not pipeline.empty():
        message = queue.get()
        logging.warning(f"Consumer storing message: {message}" +
                        f" (size={queue.qsize()})")

    logging.warning(f"Consumer received event. Exiting")

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.warning("Main: about to set event")
        event.set()


