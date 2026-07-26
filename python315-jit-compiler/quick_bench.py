"""Quick benchmark: compare CPython 3.15 with the JIT off vs on.

Run twice against the same 3.15 build and compare the two timings:

    PYTHON_JIT=0 python quick_bench.py
    PYTHON_JIT=1 python quick_bench.py
"""

import sys
from timeit import timeit

ITERATIONS = 20_000_000
REPEATS = 5


def workload():
    x = 1.0
    for _ in range(ITERATIONS):
        x = x * 1.0001
    return x


def jit_enabled():
    jit = getattr(sys, "_jit", None)
    return bool(jit and jit.is_enabled())


def main():
    seconds = timeit(workload, number=REPEATS) / REPEATS
    label = "JIT on" if jit_enabled() else "JIT off"
    print(f"{label}: {seconds:.2f} s")


if __name__ == "__main__":
    main()
