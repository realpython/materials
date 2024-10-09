import random

print("Guess my secret number!\n")
max_value = int(input("Enter maximum for the secret number: "))

print(f"Guess my number between 1 and {max_value}")
secret = random.randint(1, max_value)

while True:
    guess = int(input("Guess a number: "))
    if secret < guess:
        print(f"Sorry, my number is lower than {guess}")
    elif secret > guess:
        print(f"Sorry, my number is higher than {guess}")
    else:
        break

print(f"Yes, my number is {secret}")
