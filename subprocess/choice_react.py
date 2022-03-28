from time import sleep, time
from random import random
from string import ascii_lowercase


print(
    "A letter will appear on screen after a random amount of time,\n"
    + "when it appears, type the letter as fast as possible and then press enter\n"
)
print("Press enter when you are ready")
input()
print("Ok, get ready!")
sleep(random() * 5 + 2)
target_letter = ascii_lowercase[int(random() * 26)]
print(f"=====\n= {target_letter} =\n=====\n")

start = time()
while True:
    if input() == target_letter:
        break
    else:
        print("Nope! Try again.")
end = time()

print(f"You reacted in {end - start} seconds!\nGoodbye!")
