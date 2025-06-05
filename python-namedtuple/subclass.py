from collections import namedtuple
from datetime import date

BasePerson = namedtuple(
    "BasePerson", "name birthdate country", defaults=["Canada"]
)


class Person(BasePerson):
    """A namedtuple subclass to hold a person's data."""

    __slots__ = ()

    def __repr__(self):
        return f"Name: {self.name}, age: {self.age} years old."

    @property
    def age(self):
        return (date.today() - self.birthdate).days // 365


Person.__doc__

jane = Person("Jane", date(1996, 3, 5))
print(jane.age)
print(jane)
