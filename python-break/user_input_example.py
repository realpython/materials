# Use case 3: Getting user input

# Import the random module for generating random numbers
import random

guesses_left = 4
random_number = random.randint(1, 10)

while True:
    if guesses_left <= 0:
        print("You ran out of guesses! The correct number was " + str(random_number))
        break
    guess = input("Guess a number between 1 and 10, or enter q to quit:")
    if guess == "q":
        print("Successfully exited game.")
        break
    elif(not(guess.isnumeric())):
        guess = input("Please enter a valid value: ")
    else:
        if int(guess) == random_number:
            print("Congratulations, you picked the correct number!")
            break
        else:
            print("Sorry, your guess was incorrect.")
            guesses_left -= 1
            print("You have " + str(guesses_left) + " guesses left.")
