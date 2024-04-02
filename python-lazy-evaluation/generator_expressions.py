"""
Exploring generator expressions
"""

import random

# List comprehension
coin_toss = ["Heads" if random.random() > 0.5 else "Tails" for _ in range(10)]

print(f"List comprehension:\n{coin_toss}")

# Generator expression
coin_toss = ("Heads" if random.random() > 0.5 else "Tails" for _ in range(10))
print(f"\nGenerator expression:\n{coin_toss}")

print(f"\nFirst coin toss: {next(coin_toss)}")
print(f"Second coin toss: {next(coin_toss)}")

# Print remaining coin tosses
for toss_result in coin_toss:
    print(toss_result)

# Defining a generator function


def generate_coin_toss(number):
    for _ in range(number):
        yield "Heads" if random.random() > 0.5 else "Tails"


coin_toss = generate_coin_toss(10)
print("\nUsing a generator function:")
print(next(coin_toss))
print(next(coin_toss))

for toss_result in coin_toss:
    print(toss_result)
