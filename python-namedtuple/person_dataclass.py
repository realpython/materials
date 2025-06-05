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
