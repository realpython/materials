"""Hangman in Python for the command line."""

# To select a word at random
import string
from random import choice


def select_word() -> str:
    """Selects a random word from a list of known words.

    Returns:
        str: A word to be guessed
    """
    word_list = ["spam", "eggs", "monty", "python", "llama"]
    return choice(word_list)


def build_displayed_word(current_word: str, letters_guessed: set) -> str:
    """Builds the word to show the user
    with the corrent letters in place

    Args:
        current_word (str): What is the word?
        letters_guessed (set): Set of letters already guesses

    Returns:
        str: A string with guessed letters in the correct locations
    """

    # What do we separate the letters with
    separator = " "
    display = [
        letter if letter in letters_guessed else "*" for letter in current_word
    ]
    return separator.join(display)


def build_letter_list(letters_guessed: set) -> str:
    """Builds a displayable list of letters guessed

    Args:
        letters_guessed (set): Set letters already guessed

    Returns:
        str: A displayable string of letters
    """
    separator = " "
    return separator.join(letters_guessed)


def show_hangman(guesses: int) -> None:
    """Display the hanged man based on the number of guesses

    Args:
        guesses (int): How many guesses have been taken?
    """
    hanged_man = [
        """
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        """
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        """
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        """
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        """
  -----
  |   |
  O   |
 ---  |
/ | \\ |
  |   |
      |
      |
      |
      |
-------
""",
        """
  -----
  |   |
  O   |
 ---  |
/ | \\ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        """
  -----
  |   |
  O   |
 ---  |
/ | \\ |
  |   |
 ---  |
/   \\ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[guesses])


def game_over(
    guesses_taken: int, current_word: str, letters_guessed: set
) -> bool:
    """Determines end of game condition

    Args:
        guesses_taken (int): How many guesses have we taken?
        current_word (str): What is the word to be guessed?
        letters_guessed (set): Set of letters already guessed

    Returns:
        bool: True if the game is over, False if not
    """

    # Has the player taken all the guesses?
    if guesses_taken == 6:
        return True

    # Are all the letters in the current word all guessed?
    if set(current_word) <= letters_guessed:
        return True

    # Then the game is not over
    return False


def validate_input(player_guess: str, letters_guessed: set) -> bool:
    """Validates player input for Hangman
    This assume the player_guess is lower-case

    Args:
        player_guess (str): What did the player guess.
        letters_guessed (set): Set of letters already guessed

    Returns:
        bool: True for valid input, False if not
    """
    return (
        len(player_guess) == 1
        and player_guess in string.ascii_lowercase
        and player_guess not in letters_guessed
    )


if __name__ == "__main__":
    # Initial game setup
    # Which letters have we guessed already?
    letters_guessed = set()

    # How many guesses have they taken?
    guesses_taken = 0

    # Begin the game
    print("Welcome to Hangman!")

    # Select the word to be guessed and make a display version
    current_word = select_word()
    displayed_word = build_displayed_word(current_word, letters_guessed)

    # Begin the game loop
    while not game_over(guesses_taken, current_word, letters_guessed):
        # Show the current game state
        show_hangman(guesses_taken)
        print(f"Your word is: {displayed_word}")
        print(
            f"Current letters guessed: {build_letter_list(letters_guessed)}\n"
        )

        # Get user input and validate
        player_guess = ""
        while not validate_input(player_guess, letters_guessed):
            player_guess = str.lower(input("Guess a letter: "))

        # Is this letter in the current word?
        if player_guess in current_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            guesses_taken += 1

        # Add this letter to the set of letters guessed
        letters_guessed.add(player_guess)

        # Build the new word to be displayed
        displayed_word = build_displayed_word(current_word, letters_guessed)

    # Print the final hanged man
    show_hangman(guesses_taken)

    # If there are no more guesses, the player lost
    if guesses_taken == 6:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")

    # Show the word they were trying to guess.
    print(f"Your word was: {current_word}")
