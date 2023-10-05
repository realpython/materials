import ctypes
import os
import threading

fibonacci = ctypes.CDLL("./fibonacci.so")

fib = fibonacci.fib
fib.argtypes = (ctypes.c_int,)
fib.restype = ctypes.c_int

for _ in range(os.cpu_count()):
    threading.Thread(target=fib, args=(45,)).start()
