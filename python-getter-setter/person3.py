class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


class Employee(Person):
    def get_name(self):
        return super().get_name().upper()
