from collections import namedtuple
from pympler import asizeof

Point = namedtuple("Point", "x y z")
point = Point(1, 2, 3)

namedtuple_size = asizeof.asizeof(point)
dict_size = asizeof.asizeof(point._asdict())
gain = 100 - namedtuple_size / dict_size * 100

print(f"namedtuple: {namedtuple_size} bytes ({gain:.2f}% smaller)")
print(f"dict:       {dict_size} bytes")
