class Foo:
    pass


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new

f = Foo()
print(f.attr)

g = Foo()
print(g.attr)
