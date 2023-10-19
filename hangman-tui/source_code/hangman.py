import string
from random import choice

MAX_INCORRECT_GUESSES = 6


def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


def get_player_input(guessed_letters):
    while True:
        player_input = input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input


def _validate_input(player_input, guessed_letters):
    return (
        len(player_input) == 1
        and player_input in string.ascii_lowercase
        and player_input not in guessed_letters
    )


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)


def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
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
        r"""
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
        r"""
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
        r"""
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
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

    print(hanged_man[wrong_guesses])


def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False


if __name__ == "__main__":
    # Initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print("Welcome to Hangman!")

    # Game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        print(f"Your word is: {guessed_word}")
        print(
            "Current guessed letters: "
            f"{join_guessed_letters(guessed_letters)}\n"
        )

        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            print("Great guess!")
        else:
            print("Sorry, it's not there.")
            wrong_guesses += 1

        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # Game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        print("Sorry, you lost!")
    else:
        print("Congrats! You did it!")
    print(f"Your word was: {target_word}")
