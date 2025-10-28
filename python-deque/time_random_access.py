from collections import deque
from time import perf_counter

TIMES = 10_000
a_list = [1] * TIMES
a_deque = deque(a_list)


def average_time(func, times):
    total = 0.0
    for _ in range(times):
        start = perf_counter()
        func()
        total += (perf_counter() - start) * 1e6
    return total / times


def time_it(sequence):
    middle = len(sequence) // 2
    sequence.insert(middle, "middle")
    sequence[middle]
    sequence.remove("middle")
    del sequence[middle]


list_time = average_time(lambda: time_it(a_list), TIMES)
deque_time = average_time(lambda: time_it(a_deque), TIMES)
gain = deque_time / list_time

print(f"list  {list_time:.6} μs ({gain:.6}x faster)")
print(f"deque {deque_time:.6} μs")
