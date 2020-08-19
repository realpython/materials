"""Hangman for PySimpleGUI"""

# Imports
import PySimpleGUI as sg
from random import choice


# Hangman helper functions from Basic game
def select_word() -> str:
    """Selects a random word from a list of known words.

    Returns:
        str: A word to be guessed
    """
    word_list = ["spam", "eggs", "monty", "python", "llama"]
    return choice(word_list)


def build_displayed_word(
    current_word: str, letters_guessed: set
) -> str:
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
        letter if letter in letters_guessed else "*"
        for letter in current_word
    ]
    return separator.join(display)


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


# Hangman functions for GUI version


# PSG: Define the layout element which contains our letter buttons
def letter_frame():
    letter_groups = [
        "ABCD",
        "EFGH",
        "IJKL",
        "MNOP",
        "QRST",
        "UVWX",
        "YZ",
    ]
    return [
        [
            sg.Button(
                button_text=f" {letter} ",
                font="Courier 20",
                border_width=0,
                button_color=(None, sg.theme_background_color()),
                key=f"-letter-{letter}-",
                enable_events=True,
            )
            for letter in letter_group
        ]
        for letter_group in letter_groups
    ]


if __name__ == "__main__":

    # Create the main window layout
    layout = [
        [
            # Where do we draw the hangman?
            sg.Frame(
                "Hangman",
                [
                    [
                        sg.Graph(
                            canvas_size=(200, 400),
                            graph_bottom_left=(0, 0),
                            graph_top_right=(200, 400),
                        )
                    ]
                ],
                font="Any 20",
            ),
            # Where are the letters we can guess?
            sg.Column(
                [
                    [
                        sg.Frame(
                            "Letters", letter_frame(), font="Any 20",
                        ),
                        sg.Sizer(),
                    ]
                ]
            ),
        ],
        # Where is the word we are guessing?
        [
            sg.Frame(
                "",
                [
                    [
                        sg.Text(
                            text="* * * * * * * * * *",
                            key="-DISPLAY-WORD-",
                            font="Courier 20",
                        )
                    ]
                ],
                element_justification="center",
            )
        ],
        # A Restart and Undo button would be helpful
        [
            sg.Frame(
                "",
                [
                    [
                        sg.Sizer(h_pixels=90),
                        sg.Button(
                            button_text="Restart",
                            key="-RESTART-",
                            font="Any 20",
                        ),
                        sg.Sizer(h_pixels=60),
                        sg.Button(
                            button_text="Undo",
                            key="-UNDO-",
                            font="Any 20",
                        ),
                        sg.Sizer(h_pixels=90),
                    ]
                ],
                font="Any 20",
            ),
        ],
    ]

    # Initial game setup
    # How many guesses have they taken?
    guesses_taken = 0

    # Which letters have been guessed already
    letters_guessed = set()

    # Select the word to be guessed and make a display version
    current_word = select_word()
    displayed_word = build_displayed_word(current_word, letters_guessed)

    # Define the window
    window = sg.Window("Hangman", layout, finalize=True)

    # Undo buttom is disabled until we have a guess
    window["-UNDO-"].update(disabled=True)

    while True:
        # Display the built word
        window["-DISPLAY-WORD-"].update(displayed_word)

        # Get a button press
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        elif event[:8] == "-letter-":
            player_guess = event[8].lower()
            if player_guess not in set(current_word):
                guesses_taken += 1
            letters_guessed.add(player_guess)
            displayed_word = build_displayed_word(
                current_word, letters_guessed
            )
            window["-UNDO-"].update(disabled=False)
            window[event].update(disabled=True)

    window.close()
