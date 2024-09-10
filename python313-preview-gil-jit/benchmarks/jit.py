from argparse import ArgumentParser
from csv import DictWriter
from functools import wraps
from pathlib import Path
from time import perf_counter
from typing import NamedTuple

from pyfeatures import JitCompiler
from pyinfo import print_details, python_short

CSV_PATH = Path(__file__).with_suffix(".csv")


class Record(NamedTuple):
    python: str
    jit: str
    n: int
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
    parser.add_argument("-n", type=int, required=True)
    return parser.parse_args()


def main(args):
    print_details()
    benchmark(args.n)


def timed(function):
    jit = JitCompiler()

    @wraps(function)
    def wrapper(n):
        t1 = perf_counter()
        result = function(n)
        t2 = perf_counter()
        duration = t2 - t1
        print(f"\b\b\b: {duration:.2f}s")
        if jit.supported:
            Record(
                python_short(), "on" if jit.enabled else "off", n, duration
            ).save()
        else:
            Record(python_short(), "unsupported", n, duration).save()
        return result

    return wrapper


@timed
def benchmark(n):
    print(f"Running fib() {n:,} times...", end="", flush=True)
    for i in range(n):
        fib(i)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    main(parse_args())
