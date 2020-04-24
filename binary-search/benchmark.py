"""
Benchmark the performance of a search algorithm.

Requirements:
 * Python 3.7+

Usage:
$ python benchmark.py -a random -f names.txt 'Arnold Schwarzenegger'
$ python benchmark.py -a linear -f names.txt 'Arnold Schwarzenegger'
$ python benchmark.py -a binary -f sorted_names.txt 'Arnold Schwarzenegger'
"""

import argparse
import time
from statistics import median
from typing import List

from search.binary import find_index as binary_search
from search.random import find_index as random_search
from search.linear import find_index as linear_search


def main(args: argparse.Namespace) -> None:
    """Script entry point."""

    algorithms = {
        "random": random_search,
        "linear": linear_search,
        "binary": binary_search,
    }

    benchmark(
        algorithms[args.algorithm], load_names(args.path), args.search_term
    )


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a", "--algorithm", choices=("random", "linear", "binary")
    )
    parser.add_argument("-f", "--file", dest="path")
    parser.add_argument("search_term")
    return parser.parse_args()


def load_names(path: str) -> List[str]:
    """Return a list of names from the given file."""
    print("Loading names...", end="", flush=True)
    with open(path) as text_file:
        names = text_file.read().splitlines()
        print("ok")
        return names


def convert(nano: int) -> str:
    """Convert nano seconds to a formatted string."""

    kilo, mega, giga = 1e3, 1e6, 1e9

    if nano < kilo:
        return f"{nano} ns"

    if nano < mega:
        return f"{nano / kilo:.2f} µs"

    if nano < giga:
        return f"{nano / mega:.2f} ms"

    return f"{nano / giga:.2f} s"


def benchmark(
    algorithm, elements: List[str], value: str, repeat: int = 10
) -> None:
    """Search for a value in elements using the given algorithm."""

    times: List[int] = []
    for i in range(repeat):
        print(f"[{i + 1}/{repeat}] Searching...", end="", flush=True)
        start_time = time.perf_counter_ns()
        index = algorithm(elements, value)
        elapsed_time = time.perf_counter_ns() - start_time
        times.append(elapsed_time)
        print("\b" * 12, end="")
        if index is None:
            print(f"Not found ({convert(elapsed_time)})")
        else:
            print(f"Found at index={index} ({convert(elapsed_time)})")

    print(
        f"best={convert(min(times))}",
        f"worst={convert(max(times))}",
        f"avg={convert(int(sum(times) / len(times)))}",
        f"median={convert(int(median(times)))}",
        sep=", ",
    )


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        print("Aborted")
