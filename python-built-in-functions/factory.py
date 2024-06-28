def create_class(name, custom_members):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"{name}({self.__dict__})"

    class_members = {
        "__init__": __init__,
        "__repr__": __repr__,
    }
    class_members.update(custom_members)

    return type(name, (), class_members)


User = create_class("User", {"name": "", "age": 0, "email": ""})
Product = create_class("Product", {"name": "", "price": 0.0, "units": 0})

john = User(name="John", age=30, email="john@example.com")
table = Product(name="Table", price=200.0, units=5)
