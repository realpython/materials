import dataclasses


@dataclasses.dataclass
class Person:
    """Model a person with a name, location, and Python version."""

    name: str
    place: str
    version: str


print(Person.__doc__)

print(len(dataclasses.replace.__doc__))
print(dataclasses.replace.__doc__)
