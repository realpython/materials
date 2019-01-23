#!/usr/bin/env python3
import concurrent.futures
import threading
import time

class FakeDatabase():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def lock_database(self):
        self._lock.acquire()

    def unlock_database(self):
        self._lock.release()



def bad_thread_function(database):
    name = threading.current_thread().name
    local_copy = database.get_value()
    local_copy += 1
    print(f"Thread {name}: starting")
    time.sleep(0.1)
    print(f"Thread {name}: finishing")
    database.set_value(local_copy)


def fixed_thread_function(database):
    name = threading.current_thread().name
    print(f"{name} about to lock")
    database.lock_database()
    print(f"{name} after lock")
    try:
        print(f"Thread {name}: starting")
        local_copy = database.get_value()
        local_copy += 1
        time.sleep(0.1)
        database.set_value(local_copy)
        print(f"Thread {name}: finishing")
    finally:
        print(f"{name} about to release")
        database.unlock_database()
        print(f"{name} after release")



if __name__ == "__main__":
    database = FakeDatabase()
    print(f"At the start, database has {database.get_value()}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for _ in range(2):
            # executor.submit(bad_thread_function, database)
            executor.submit(fixed_thread_function, database)
    print(f"At the end, database has {database.get_value()}.")

