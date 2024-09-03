from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from csv import DictWriter
from functools import wraps
from os import cpu_count
from pathlib import Path
from time import perf_counter
from typing import NamedTuple

from pyinfo import print_details, python_short

CSV_PATH = Path(__file__).with_suffix(".csv")
DEFAULT_N = 35


class Record(NamedTuple):
    python: str
    threads: int
    seconds: float

    def save(self):
        empty = not CSV_PATH.exists()
        with CSV_PATH.open(mode="a", encoding="utf-8", newline="") as file:
            writer = DictWriter(file, Record._fields)
            if empty:
                writer.writeheader()
            writer.writerow(self._asdict())


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-t", "--threads", type=int, default=cpu_count())
    parser.add_argument("-n", type=int, default=DEFAULT_N)
    return parser.parse_args()


def main(args):
    print_details()
    benchmark(args.threads, args.n)


def timed(function):
    @wraps(function)
    def wrapper(num_threads, n):
        t1 = perf_counter()
        result = function(num_threads, n)
        t2 = perf_counter()
        duration = t2 - t1
        print(f"\b\b\b: {duration:.2f}s")
        Record(python_short(), num_threads, duration).save()
        return result

    return wrapper


@timed
def benchmark(num_threads, n):
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for _ in range(num_threads):
            executor.submit(fib, n)
        if num_threads > 1:
            print(f"Running {num_threads} threads...", end="", flush=True)
        else:
            print("Running 1 thread...", end="", flush=True)


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    main(parse_args())
