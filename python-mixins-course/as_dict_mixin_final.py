class AsDictMixin:
    def as_dict(self):
        return vars(self)


class Person(AsDictMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 42)
print(john.as_dict())


class Car(AsDictMixin):
    def __init__(self, make, model):
        self.make = make
        self.model = model


toyota = Car("Toyota", "Prius")
print(toyota.as_dict())