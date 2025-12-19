from collections import deque
from time import perf_counter

TIMES = 10_000
NANOSECONDS_PER_SECOND = 1e9
a_list = []
a_deque = deque()


def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        # Convert to ns to improve readability
        total += (perf_counter() - start) * NANOSECONDS_PER_SECOND
    return total / times


list_time = average_time(lambda i: a_list.insert(0, i), TIMES)
deque_time = average_time(lambda i: a_deque.appendleft(i), TIMES)
gain = list_time / deque_time

print(f"list.insert()      {list_time:.6} ns")
print(f"deque.appendleft() {deque_time:.6} ns  ({gain:.6}x faster)")
