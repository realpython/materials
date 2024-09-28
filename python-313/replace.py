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


# %% Create a custom class that supports copy.replace()
class NamedContainer:
    def __init__(self, name, **items):
        print(f"Initializing {name} with {items}")
        self.name = name
        self.items = items

    def __replace__(self, **kwargs):
        """.__replace__() is called by copy.replace()"""
        if "name" in kwargs:
            raise ValueError("'name' can't be updated")

        print(f"Replacing {kwargs} in {self.name}")
        init_kwargs = {"name": self.name} | self.items | kwargs

        # Create a new object with updated arguments
        cls = type(self)
        return cls(**init_kwargs)

    def __repr__(self):
        items = [f"{key}={value!r}" for key, value in self.items.items()]
        return f"{type(self).__name__}(name='{self.name}', {", ".join(items)})"


capitals = NamedContainer(
    "capitals", norway="oslo", sweden="Stockholm", denmark="Copenhagen"
)
print(f"{capitals = }")

capitals = copy.replace(capitals, norway="Oslo")
print(f"{capitals = }")

# copy.replace(capitals, name="Scandinavia")  # Raises an error, name can't be replaced
