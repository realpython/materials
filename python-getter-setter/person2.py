class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Employee(Person):
    @property
    def name(self):
        return super().name.upper()
