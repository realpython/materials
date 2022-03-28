from time import sleep, time
from random import random

print("Press enter to play")
input()
print("Ok, get ready!")
sleep(random() * 5 + 1)
print("go!")
start = time()
input()
end = time()
print(f"You reacted in {end - start} seconds!\nGoodbye!")
