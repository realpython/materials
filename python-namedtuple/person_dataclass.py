from dataclasses import astuple, dataclass


@dataclass
class Person:
    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"

    def __iter__(self):
        return iter(astuple(self))


jane = Person("Jane", 25, 1.75, 67)
for field in jane:
    print(field)
