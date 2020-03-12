from timeit import timeit
def test_iterating(iterable):
    for i in iterable:
            pass

# set
timeit("test_iterating(iterable)", setup="from __main__ import test_iterating; iterable = set(range(10000))", number=10000)

# list
timeit("test_iterating(iterable)", setup="from __main__ import test_iterating; iterable = list(range(10000))", number=10000)

# lookups
def test_lookups(iterable):
    for i in range(1000):
            if i in iterable:
                    pass

# set
timeit("test_lookups(iterable)", setup="from __main__ import test_lookups; iterable = set(range(10000))", number=10000)

# list
timeit("test_lookups(iterable)", setup="from __main__ import test_lookups; iterable = list(range(10000))", number=10000)
