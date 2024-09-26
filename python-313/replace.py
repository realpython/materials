import copy
from datetime import date
from typing import NamedTuple


class Person(NamedTuple):
    name: str
    place: str
    version: str


person = Person(name="Geir Arne", place="Oslo", version="3.12")
person = Person(name=person.name, place=person.place, version="3.13")
print(person)

today = date.today()
print(today)
print(today.replace(day=1))
print(today.replace(month=12, day=24))

person = Person(name="Geir Arne", place="Oslo", version="3.12")
print(copy.replace(person, version="3.13"))
print(copy.replace(today, day=1))
