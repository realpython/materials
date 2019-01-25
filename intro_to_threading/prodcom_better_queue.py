#!/usr/bin/env python3
import concurrent.futures
import queue
import random
import threading
import time


def producer(queue, event):
    '''Pretend we're getting a number from the network.'''
    while not event.is_set():
        new_datapoint = random.randint(1,101)
        print(f"Producer got data {new_datapoint}")
        queue.put(new_datapoint)

    print(f"Producer received event. Exiting")

def consumer(queue, event):
    ''' Pretend we're saving a number in the database. '''
    while not event.is_set() or not pipeline.empty():
        datapoint = queue.get()
        print(f"Consumer storing data: {datapoint}" +
                        f" (size={queue.qsize()})")

    print(f"Consumer received event. Exiting")


if __name__ == "__main__":
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        print("Main: about to set event")
        event.set()


