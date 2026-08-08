import timeit
from functools import cache

numbers = list(range(2_000_000))


def find_index(target):
    for i, value in enumerate(numbers):
        if value == target:
            return i
    return -1


target = 1_999_999

print(find_index(target))

slow_time = timeit.timeit(lambda: find_index(target), number=20)
print(f"without cache: {slow_time:.4f} seconds")


@cache
def find_index_cached(target):
    for i, value in enumerate(numbers):
        if value == target:
            return i
    return -1


print(find_index_cached(target))

fast_time = timeit.timeit(lambda: find_index_cached(target), number=20)
print(f"with cache: {fast_time:.8f} seconds")
