def f(obj):
    print("attr =", obj.attr)


# Defining the class dynamically with type()
Foo = type("Foo", (), {"attr": 100, "attr_val": f})

x = Foo()
print(x.attr)
x.attr_val()


# The same class defined the usual way, with the class statement
class Foo:
    attr = 100
    attr_val = f


x = Foo()
print(x.attr)
x.attr_val()
