import random

num = random.randint(1, 100)
i = None

while i != num:
    i = int(input("Guess the number: "))
    if i < num:
        print("Too low")
    elif i > num:
        print("Too high")
    else:
        print("Correct!")
