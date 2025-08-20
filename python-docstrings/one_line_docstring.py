import random


def picking_hat():
    """Return a random house name."""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    return random.choice(houses)
