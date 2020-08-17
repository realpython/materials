import PySimpleGUI as sg
from random import choice

# Hangman globals
word_list = ["foolish", "gambler", "truncate", "boor"]
letters_guessed = set()
guesses_remaining = 6
current_word = ""
displayed_word = ""
separator = " "

# Hangman helper functions
def build_displayed_word(word):
    display = []
    for letter in word:
        if letter in letters_guessed:
            display.append(letter)
        else:
            display.append("*")
    return separator.join(display)


def game_over():
    if guesses_remaining == 0:
        return True

    if set(current_word) <= letters_guessed:
        return True

    return False


def get_longest_word():
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return build_displayed_word(longest_word)


# PSG: Define the layout element which contains our letter buttons
def letter_frame():
    letter_groups = ["ABCD", "EFGH", "IJKL", "MNOP", "QRST", "UVWX", "YZ"]
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
                    sg.Frame("Letters", letter_frame(), font="Any 20",),
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
                        text=get_longest_word(),
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
                        button_text="Restart", key="-RESTART-", font="Any 20"
                    ),
                    sg.Sizer(h_pixels=60),
                    sg.Button(button_text="Undo", key="-UNDO-", font="Any 20"),
                    sg.Sizer(h_pixels=90),
                ]
            ],
            font="Any 20",
        ),
    ],
]

# Define the window
window = sg.Window("Hangman", layout, finalize=True)

# Setup the game

current_word = choice(word_list)
displayed_word = build_displayed_word(current_word)

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
            guesses_remaining -= 1
        letters_guessed.add(player_guess)
        displayed_word = build_displayed_word(current_word)
        window["-UNDO-"].update(disabled=False)
        window[event].update(disabled=True)



window.close()
