#!/usr/bin/env python3
import concurrent.futures
import logging
import threading
import time

class FakeDatabase():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.warning(f"Thread {name}: starting update")
        logging.debug(f"Thread {name} about to lock")
        with self._lock:
            logging.debug(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug(f"Thread {name} about to release lock")
        logging.debug(f"Thread {name} after release")
        logging.warning(f"Thread {name}: finishing update")

if __name__ == "__main__":
    logging.basicConfig(format='%(message)s')
    logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()
    logging.warning(f"Testing locked update. Starting value is {database.value}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.warning(f"Testing locked update. Ending value is {database.value}.")
