from collections import namedtuple
from time import perf_counter


def average_time(structure, test_func):
    time_measurements = []
    for _ in range(1_000_000):
        start = perf_counter()
        test_func(structure)
        end = perf_counter()
        time_measurements.append(end - start)
    return sum(time_measurements) / len(time_measurements) * int(1e9)


def time_dict(dictionary):
    "x" in dictionary
    "missing_key" in dictionary
    2 in dictionary.values()
    "missing_value" in dictionary.values()
    dictionary["y"]


def time_namedtuple(named_tuple):
    "x" in named_tuple._fields
    "missing_field" in named_tuple._fields
    2 in named_tuple
    "missing_value" in named_tuple
    named_tuple.y


Point = namedtuple("Point", "x y z")
point = Point(x=1, y=2, z=3)

namedtuple_time = average_time(point, time_namedtuple)
dict_time = average_time(point._asdict(), time_dict)
gain = dict_time / namedtuple_time

print(f"namedtuple: {namedtuple_time:.2f} ns ({gain:.2f}x faster)")
print(f"dict:       {dict_time:.2f} ns")
