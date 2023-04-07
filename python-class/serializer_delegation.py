import json
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Serializer:
    def __init__(self, instance):
        self.instance = instance

    def to_json(self):
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __getattr__(self, attr):
        return getattr(Serializer(self), attr)
