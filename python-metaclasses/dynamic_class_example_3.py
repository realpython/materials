# Defining the class dynamically with type()
Foo = type("Foo", (), {"attr": 100, "attr_val": lambda x: x.attr})

x = Foo()
print(x.attr)
print(x.attr_val())


# The same class defined the usual way, with the class statement
class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


x = Foo()
print(x.attr)
print(x.attr_val())
