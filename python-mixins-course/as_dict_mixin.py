class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def as_dict(self):
        return {
            "name": self.name,
            "age": self.age,
        }


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def as_dict(self):
        return {
            "make": self.make,
            "model": self.model,
        }