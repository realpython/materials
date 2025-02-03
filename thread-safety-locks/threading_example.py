import threading
import time
from concurrent.futures import ThreadPoolExecutor


def threaded_function():
    for number in range(3):
        print(f"Printing from {threading.current_thread().name}. {number=}")
        time.sleep(0.1)


with ThreadPoolExecutor(
    max_workers=4, thread_name_prefix="Worker"
) as executor:
    for _ in range(4):
        executor.submit(threaded_function)
