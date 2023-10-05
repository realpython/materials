import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def echo(data):
    return data


if __name__ == "__main__":
    data = [complex(i, i) for i in range(15_000_000)]
    for executor in ThreadPoolExecutor(), ProcessPoolExecutor():
        t1 = time.perf_counter()
        with executor:
            future = executor.submit(echo, data)
            future.result()
        t2 = time.perf_counter()
        print(f"{type(executor).__name__:>20s}: {t2 - t1:.2f}s")
