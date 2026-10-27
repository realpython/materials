# Defining the class dynamically with type()
Foo = type("Foo", (), {})

x = Foo()
print(x)


# The same class defined the usual way, with the class statement
class Foo:
    pass


x = Foo()
print(x)
