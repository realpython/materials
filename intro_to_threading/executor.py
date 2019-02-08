#!/usr/bin/env python3
import concurrent.futures
import logging
import threading
import time

def thread_function(name):
    logging.warning(f"Thread {name}: starting")
    time.sleep(2)
    logging.warning(f"Thread {name}: finishing")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(3))

