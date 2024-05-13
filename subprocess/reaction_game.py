"""
Tests your reaction times.

Note: This game can be cheated by pressing enter before the game prompts you
to press enter.
"""

from random import random
from time import perf_counter, sleep

print("Press enter to play")
input()
print("Ok, get ready!")
sleep(random() * 5 + 1)
print("go!")
start = perf_counter()
input()
end = perf_counter()
print(f"You reacted in {(end - start) * 1000:.0f} milliseconds!\nGoodbye!")
