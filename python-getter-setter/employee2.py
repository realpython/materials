from datetime import date


class Employee:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = date.fromisoformat(value)
