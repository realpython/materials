from collections import namedtuple

STest = namedtuple("TEST", "a b c")
a = STest(a=1, b=2, c=3)


class Test(object):
    __slots__ = ["a", "b", "c"]

    def __init__(self) -> None:
        self.a = 1
        self.b = 2
        self.c = 3


b = Test()

c = {"a": 1, "b": 2, "c": 3}

d = (1, 2, 3)
e = [1, 2, 3]
f = (1, 2, 3)
g = [1, 2, 3]
key = 2

if __name__ == "__main__":
    from timeit import timeit

    print("Named tuple with a, b, c:")
    print(timeit("z = a.c", "from __main__ import a"))

    print("Named tuple, using index:")
    print(timeit("z = a[2]", "from __main__ import a"))

    print("Class using __slots__, with a, b, c:")
    print(timeit("z = b.c", "from __main__ import b"))

    print("Dictionary with keys a, b, c:")
    print(timeit("z = c['c']", "from __main__ import c"))

    print("Tuple with three values, using a constant key:")
    print(timeit("z = d[2]", "from __main__ import d"))

    print("List with three values, using a constant key:")
    print(timeit("z = e[2]", "from __main__ import e"))

    print("Tuple with three values, using a local key:")
    print(timeit("z = d[key]", "from __main__ import d, key"))

    print("List with three values, using a local key:")
    print(timeit("z = e[key]", "from __main__ import e, key"))
