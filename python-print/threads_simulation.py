import sys
from random import random
from threading import Thread, current_thread
from time import sleep
from unittest.mock import patch

write = sys.stdout.write


def slow_write(text):
    sleep(random())
    write(text)


def task():
    thread_name = current_thread().name
    for letter in "ABC":
        # print(f"[{thread_name} {letter}]")
        print(f"[{thread_name} {letter}]\n", end="")


with patch("sys.stdout") as mock_stdout:
    mock_stdout.write = slow_write
    for i in range(1, 4):
        Thread(target=task, name=f"Thread-{i}").start()
