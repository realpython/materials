import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("You got it!")
else:
    print(f"Sorry, the number was {number}.")
