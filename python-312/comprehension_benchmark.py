import sys
import timeit
from functools import partial

NUM_REPEATS = 100


def convert_unit(value):
    for unit in ["s", "ms", "μs", "ns"]:
        if value > 1:
            return f"{value:8.2f}{unit}"
        value *= 1000


def timer(func):
    def _timer(*args, **kwargs):
        tictoc = timeit.timeit(
            partial(func, *args, **kwargs), number=NUM_REPEATS
        )
        print(f"{func.__name__:<20} {convert_unit((tictoc) / NUM_REPEATS)}")

    return _timer


@timer
def plain(numbers):
    return [number for number in numbers]


@timer
def square(numbers):
    return [number**2 for number in numbers]


@timer
def filtered(numbers):
    return [number for number in numbers if number % 2 == 0]


n, N = 100, 100_000
small_numbers = range(n)
big_numbers = range(N)
repeated_numbers = [1 for _ in range(N)]

print(sys.version)

print("\nOne item iterable:")
plain([0])
square([0])
filtered([0])

print(f"\nSmall iterable ({n = :,}):")
plain(small_numbers)
square(small_numbers)
filtered(small_numbers)

print(f"\nBig iterable ({N = :,}):")
plain(big_numbers)
square(big_numbers)
filtered(big_numbers)

print(f"\nRepeated iterable ({N = :,}):")
plain(repeated_numbers)
square(repeated_numbers)
filtered(repeated_numbers)
