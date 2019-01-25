#!/usr/bin/env python3
import concurrent.futures
import threading
import time

class FakeDatabase():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        local_copy = self.value
        local_copy += 1
        print(f"Thread {name}: starting")
        time.sleep(0.1)
        print(f"Thread {name}: finishing")
        self.value = local_copy

    def locked_update(self, name):
        print(f"Thread {name} about to lock")
        with self._lock:
            print(f"Thread {name} has lock")
            self.update(name)
            print(f"Thread {name} about to release lock")
        print(f"Thread {name} after release")

if __name__ == "__main__":
    database = FakeDatabase()
    print(f"Testing unlocked update. Starting value is {database.value}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    print(f"Testing unlocked update. Ending value is {database.value}.")

    print("\nReset value in our fake database\n")
    database.value = 0

    print(f"Testing locked update. Starting value is {database.value}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    print(f"Testing locked update. Ending value is {database.value}.")

