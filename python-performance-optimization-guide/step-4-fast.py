import timeit

numbers = list(range(2_000_000))
target = 1_999_999

from functools import cache


@cache
def find_index_cached(target):
    for i, value in enumerate(numbers):
        if value == target:
            return i
    return -1


print(find_index_cached(target))

fast_time = timeit.timeit(lambda: find_index_cached(target), number=20)
print(f"with cache: {fast_time:.8f} seconds")
