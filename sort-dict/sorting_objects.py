from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    family: str


farm = {
    "house_guard": Animal("Bill", "Mammal"),
    "companion": Animal("Steve", "Reptile"),
    "retriever": Animal("Timmy", "Dinosaur"),
    "gate_guard": Animal("Pepe", "Insect"),
}


def sort_by_strength(animal_tuple):
    order = ["Dinosaur", "Reptile", "Mammal", "Insect"]
    return order.index(animal_tuple[1].family)


print(dict(sorted(farm.items(), key=sort_by_strength)))
