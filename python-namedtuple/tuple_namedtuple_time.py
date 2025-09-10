from collections import namedtuple
from time import perf_counter


def average_time(test_func):
    time_measurements = []
    for _ in range(1_000):
        start = perf_counter()
        test_func()
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(1e9)


def time_tuple():
    tuple([1] * 1000)


fields = [f"a{n}" for n in range(1000)]
TestNamedTuple = namedtuple("TestNamedTuple", fields)


def time_namedtuple():
    TestNamedTuple(*([1] * 1000))


namedtuple_time = average_time(time_namedtuple)
tuple_time = average_time(time_tuple)
gain = namedtuple_time / tuple_time

print(f"tuple:      {tuple_time:.2f} ns ({gain:.2f}x faster)")
print(f"namedtuple: {namedtuple_time:.2f} ns")
