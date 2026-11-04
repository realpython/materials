"""Hangman for PySimpleGUI."""

# Imports
from random import choice

import PySimpleGUI as sg


# Hangman helper functions from Basic game
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


def draw_hangman(graph_element: sg.Graph, guesses_taken: int) -> None:
    """Draw the proper Hangman

    Args:
        graph_element (sg.Graph): Where to draw the hangman
        guesses_taken (int): How far do we draw them
    """

    # Clear the screen
    graph_element.Erase()

    # Draw the scaffold
    graph_element.DrawLine([40, 55], [180, 55], width=10)
    graph_element.DrawLine([165, 60], [165, 365], width=10)
    graph_element.DrawLine([160, 360], [100, 360], width=10)
    graph_element.DrawLine([100, 365], [100, 330], width=10)
    graph_element.DrawLine([100, 330], [100, 310], width=1)

    # Draw the hanged man
    if guesses_taken >= 1:
        # Draw the head
        graph_element.DrawCircle(
            [100, 290], 20, line_color="red", line_width=1
        )

    if guesses_taken >= 2:
        # Draw the body
        graph_element.DrawLine([100, 270], [100, 170], color="red", width=1)

    if guesses_taken >= 3:
        # Draw the left arm
        graph_element.DrawLine([100, 250], [80, 250], color="red", width=1)
        graph_element.DrawLine([80, 250], [60, 210], color="red", width=1)
        graph_element.DrawLine([60, 210], [60, 190], color="red", width=1)

    if guesses_taken >= 4:
        # Draw the right arm
        graph_element.DrawLine([100, 250], [120, 250], color="red", width=1)
        graph_element.DrawLine([120, 250], [140, 210], color="red", width=1)
        graph_element.DrawLine([140, 210], [140, 190], color="red", width=1)

    if guesses_taken >= 5:
        # Draw the left leg
        graph_element.DrawLine([100, 170], [80, 170], color="red", width=1)
        graph_element.DrawLine([80, 170], [70, 140], color="red", width=1)
        graph_element.DrawLine([70, 140], [70, 80], color="red", width=1)
        graph_element.DrawLine([70, 80], [60, 80], color="red", width=1)

    if guesses_taken >= 6:
        # Draw the right leg
        graph_element.DrawLine([100, 170], [120, 170], color="red", width=1)
        graph_element.DrawLine([120, 170], [130, 140], color="red", width=1)
        graph_element.DrawLine([130, 140], [130, 80], color="red", width=1)
        graph_element.DrawLine([130, 80], [140, 80], color="red", width=1)


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
                            key="-HANGMAN-",
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
                            "Letters",
                            letter_frame(),
                            font="Any 20",
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
        # New, Restart, and Quit buttons
        [
            sg.Frame(
                "",
                [
                    [
                        sg.Sizer(h_pixels=90),
                        sg.Button(
                            button_text="New",
                            key="-NEW-",
                            font="Any 20",
                        ),
                        sg.Sizer(h_pixels=60),
                        sg.Button(
                            button_text="Restart",
                            key="-RESTART-",
                            font="Any 20",
                        ),
                        sg.Sizer(h_pixels=60),
                        sg.Button(
                            button_text="Quit",
                            key="-QUIT-",
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

    # Did the user quit the game?
    player_quit = False

    # Start the game/event loop
    while not game_over(guesses_taken, current_word, letters_guessed):
        # Display the built word
        window["-DISPLAY-WORD-"].update(displayed_word)

        # Draw the hanged man
        draw_hangman(window["-HANGMAN-"], guesses_taken)

        # Get a button press
        event, values = window.read()

        # Does the user want to close the window?
        if event in (sg.WIN_CLOSED, "Exit", "-QUIT-"):
            player_quit = True
            break

        # Was it a letter button?
        elif event[:8] == "-letter-":
            # Which letter?
            player_guess = event[8].lower()

            # Is it in the word?
            if player_guess not in current_word:
                guesses_taken += 1

            # Add it to the letters guessed
            letters_guessed.add(player_guess)

            # Build a new display word
            displayed_word = build_displayed_word(
                current_word, letters_guessed
            )

            # Disable this letter button
            window[event].update(disabled=True)

        # Was it the restart button?
        elif event == "-RESTART-":
            # Clear the letters guessed
            letters_guessed.clear()

            # Reset the number of guesses taken
            guesses_taken = 0

            # Build a new display word
            displayed_word = build_displayed_word(
                current_word, letters_guessed
            )

            # Enable all the letter buttons
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                window[f"-letter-{letter}-"].update(disabled=False)

        # Was it the New button?
        elif event == "-NEW-":
            # Select a new word
            current_word = select_word()

            # Clear the letters guessed
            letters_guessed.clear()

            # Reset the number of guesses taken
            guesses_taken = 0

            # Build a new display word
            displayed_word = build_displayed_word(
                current_word, letters_guessed
            )

            # Enable all the letter buttons
            for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                window[f"-letter-{letter}-"].update(disabled=False)

    # Draw the final hanged man
    draw_hangman(window["-HANGMAN-"], guesses_taken)

    # Display the built word
    window["-DISPLAY-WORD-"].update(displayed_word)

    # Did the player quit?
    if player_quit:
        pass

    # Did the player win?
    elif guesses_taken < 6:
        sg.Popup(
            "You've won! Congratulations!",
            title="Winner!",
            custom_text="OK",
        )
    else:
        sg.Popup(
            f"You've lost! The word was '{current_word}'.",
            title="Sorry!",
            custom_text="OK",
        )

    window.close()
