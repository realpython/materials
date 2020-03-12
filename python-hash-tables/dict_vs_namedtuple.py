from collections import namedtuple
Car = namedtuple('Car', ['name', 'color', 'size'])
car_tuple = Car(name="Toyota", color="black", size="big")
car_dict = {"name": "Toyota", "color": "black", "size": "big"}

type_ = namedtuple("test", [f"t{i}" for i in range(1000)])
t1 = type_(*list(range(1000)))
d1 = {f"t{i}": 0 for i in range(1000)}

# namedtuple
print(timeit("test_lookups(iterable)", setup="from __main__ import test_lookups, t1; iterable = t1", number=10000))

# dict
print(timeit("test_lookups(iterable)", setup="from __main__ import test_lookups, d1; iterable = d1", number=10000))
