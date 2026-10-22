class Foo:
    pass


x = Foo()
print(type(x))
print(type(Foo))

for t in int, float, dict, list, tuple:
    print(type(t))

print(type(type))
