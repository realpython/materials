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

    logging.warning("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=[1,], daemon=True)
    logging.warning("Main    : before running thread")
    x.start()
    logging.warning("Main    : wait for the thread to finish")
    x.join()
    logging.warning("Main    : all done")

