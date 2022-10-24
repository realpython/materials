from datetime import date


class Date:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = date.fromisoformat(value)


class Employee:
    birth_date = Date()
    start_date = Date()

    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()
