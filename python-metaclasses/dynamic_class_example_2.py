# Foo comes from Example 1
Foo = type("Foo", (), {})

# Defining the class dynamically with type()
Bar = type("Bar", (Foo,), dict(attr=100))

x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


# The same class defined the usual way, with the class statement
class Bar(Foo):
    attr = 100


x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)
