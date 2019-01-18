#!/usr/bin/env python3
import concurrent.futures
import threading
import time

fake_database_access = 0

def thread_function(name):
    global fake_database_access
    local_copy = fake_database_access
    local_copy += 1
    print(f"Thread {name}: starting")
    time.sleep(0.1)
    print(f"Thread {name}: finishing")
    fake_database_access = local_copy


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(2))
    print(f"At the end, database has {fake_database_access}.")

