# Slicing

game_name = "Stardew Valley"
print(game_name[:4])

# Multi-Sequence Iteration

pets = ["Leo", "Aubrey", "Frieda"]
owners = ["Bartosz", "Sarah Jane", "Philipp"]

for pet, owner in zip(pets, owners):
    print(f"{pet} & {owner}")

# Advanced Iteration Patterns

from itertools import pairwise

cities = ["Graz", "Belgrade", "Warsaw", "Berlin"]

for city, next_city in pairwise(cities):
    print(f"{city} -> {next_city}")
