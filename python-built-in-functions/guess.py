from random import randint

LOW, HIGH = 1, 10

secret_number = randint(LOW, HIGH)
clue = ""

while True:
    guess = input(f"Guess a number between {LOW} and {HIGH} {clue} ")
    number = int(guess)
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        break

print(f"You guessed it! The secret number is {number}")
