import os
import threading


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


for _ in range(os.cpu_count()):
    threading.Thread(target=fib, args=(35,)).start()
