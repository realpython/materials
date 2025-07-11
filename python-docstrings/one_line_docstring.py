import random


def picking_hat():
    """Returns a random house name."""
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    return random.choice(houses)
