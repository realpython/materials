#!/usr/bin/env python3
import logging
import threading
import time

def thread_function(name):
    logging.warning(f"Thread {name}: starting")
    time.sleep(2)
    logging.warning(f"Thread {name}: finishing")


if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')

    threads = list()
    for index in range(3):
        logging.warning(f"Main    : create and start thread {index}.")
        x = threading.Thread(target=thread_function, args=[index, 3, 4])
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.warning(f"Main    : before joining thread {index}.")
        thread.join()
        logging.warning(f"Main    : thread {index} done")
