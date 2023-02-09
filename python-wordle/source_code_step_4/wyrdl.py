import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))


def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n"))
    guesses = ["_" * 5] * 6

    # Process (main loop)
    for idx in range(6):
        refresh_page(headline=f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = input("\nGuess word: ").upper()
        if guesses[idx] == word:
            break

    # Post-process
    game_over(guesses, word, guessed_correctly=guesses[idx] == word)


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")


def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

        console.print("".join(styled_guess), justify="center")


def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")


if __name__ == "__main__":
    main()
