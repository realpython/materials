from concurrent.futures import (
    InterpreterPoolExecutor,
    ProcessPoolExecutor,
    ThreadPoolExecutor,
)
from time import perf_counter

MAX_VALUE = 35
NUM_VALUES = 4
NUM_WORKERS = 4


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


def compute(Pool):
    t1 = perf_counter()
    with Pool(max_workers=NUM_WORKERS) as pool:
        list(pool.map(fib, [MAX_VALUE] * NUM_VALUES))
    t2 = perf_counter()
    print(f"{Pool.__name__}: {(t2 - t1):.2f}s")


if __name__ == "__main__":
    compute(InterpreterPoolExecutor)
    compute(ProcessPoolExecutor)
    compute(ThreadPoolExecutor)
