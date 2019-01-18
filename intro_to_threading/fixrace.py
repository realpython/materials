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
        self._lock_release()



def bad_thread_function(name, database):
    local_copy = database.get_value()
    local_copy += 1
    print(f"Thread {name}: starting")
    time.sleep(0.1)
    print(f"Thread {name}: finishing")
    database.set_value(local_copy)


def fixed_thread_function(name, database):

    database.lock_database()
    local_copy = database.get_value()
    local_copy += 1
    print(f"Thread {name}: starting")
    time.sleep(0.1)
    print(f"Thread {name}: finishing")
    database.set_value()
    database.release_database()


if __name__ == "__main__":
    database = FakeDatabase()
    print(f"At the start, database has {database.get_value()}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(2):
            # executor.submit(bad_thread_function, index, database)
            executor.submit(fixed_thread_function, index, database)
        # executor.map(thread_function, range(2))
    print(f"At the end, database has {database.get_value()}.")

