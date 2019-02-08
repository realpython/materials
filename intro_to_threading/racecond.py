#!/usr/bin/env python3
import concurrent.futures
import logging
import threading
import time

class FakeDatabase():
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.warning(f"Thread {name}: starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.warning(f"Thread {name}: finishing update")

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')

    database = FakeDatabase()
    logging.warning(f"Testing update. Starting value is {database.value}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.warning(f"Testing update. Ending value is {database.value}.")
