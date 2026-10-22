class Foo:
    pass


obj = Foo()
print(obj.__class__)
print(type(obj))
print(obj.__class__ is type(obj))

n = 5
d = {"x": 1, "y": 2}
x = Foo()

for obj in (n, d, x):
    print(type(obj) is obj.__class__)
