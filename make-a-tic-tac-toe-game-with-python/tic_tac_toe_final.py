import io

import PySimpleGUI as sg
from PIL import Image

PLAYER_X_IMAGE_PATH = "assets/X.png"
PLAYER_O_IMAGE_PATH = "assets/O.png"
BLANK_IMAGE_PATH = "assets/BLANK.png"
INITIAL_PLAYER = "X"


def ask_if_play_again(player):
    """
    Ask the user if they want to play again or quit
    """
    if player is None:
        message = "Tied Game!"
    else:
        message = f"{player} won!"
    layout = [
        [sg.Text(f"{message} Do you want to play again or Quit?")],
        [sg.Button("Restart"), sg.Button("Quit")],
    ]
    event, values = sg.Window("Play Again?", layout, modal=True).read(
        close=True
    )
    return True if event == "Restart" else False


def check_if_won(winning_configurations):
    """
    Check if anyone has won yet
    """
    winner = None
    for configuration in winning_configurations:
        game_pieces = {btn.metadata for btn in configuration}
        is_won = None not in game_pieces and len(game_pieces) == 1
        if is_won:
            winner = game_pieces.pop()
            mark_win([*configuration])
            return (True, winner)

    # Check if tied game
    data = [
        btn.metadata
        for configuration in winning_configurations
        for btn in configuration
    ]

    if None not in data:
        # Tied game
        return (None, winner)

    # Keep playing
    return (False, winner)


def get_winning_configurations(buttons):
    """
    Returns a list of methods to win the game
    """
    horizontal_ways_to_win = [
        [buttons[0][0], buttons[1][0], buttons[2][0]],
        [buttons[0][1], buttons[1][1], buttons[2][1]],
        [buttons[0][2], buttons[1][2], buttons[2][2]],
    ]
    vertical_ways_to_win = [
        [buttons[0][0], buttons[0][1], buttons[0][2]],
        [buttons[1][0], buttons[1][1], buttons[1][2]],
        [buttons[2][0], buttons[2][1], buttons[2][2]],
    ]
    diagonal_ways_to_win = [
        [buttons[0][0], buttons[1][1], buttons[2][2]],
        [buttons[0][2], buttons[1][1], buttons[2][0]],
    ]
    return horizontal_ways_to_win + vertical_ways_to_win + diagonal_ways_to_win


def mark_win(buttons):
    """
    Mark the winning buttons with a different background color
    """
    for button in buttons:
        button.update(button_color=["green", "green"])


def reset_game(buttons):
    """
    Reset the game to play again
    """
    bio = io.BytesIO()
    image = Image.open(BLANK_IMAGE_PATH)
    image.save(bio, format="PNG")
    for row in buttons:
        for button in row:
            button.update(
                image_data=bio.getvalue(), button_color=["white", "white"]
            )
            button.metadata = None


def update_game(button, player):
    """
    Update the game
    """
    original_player = player
    if player == "X":
        filename = PLAYER_X_IMAGE_PATH
        player = "O"
    else:
        filename = PLAYER_O_IMAGE_PATH
        player = "X"

    bio = io.BytesIO()
    image = Image.open(filename)
    image.save(bio, format="PNG")

    if not button.metadata:
        button.update(text=player, image_data=bio.getvalue())
        button.metadata = original_player
        return player

    return original_player


def main():
    """
    Create GUI and manage UI events
    """
    layout = [
        [
            sg.Button(
                size=(7, 5),
                button_text=f"({row} {col})",
                key=(row, col),
                button_color=("white", "white"),
                image_filename=BLANK_IMAGE_PATH,
            )
            for row in range(3)
        ]
        for col in range(3)
    ]
    window = sg.Window("Tic-Tac-Toe", layout)
    ways_to_win = get_winning_configurations(layout)

    player = INITIAL_PLAYER
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if isinstance(event, tuple):
            btn_clicked = window[event]
            player = update_game(btn_clicked, player)
            winning_configuration, winner = check_if_won(ways_to_win)
            if winning_configuration is not False:
                should_restart = ask_if_play_again(winner)
                if should_restart is False:
                    # Close the application
                    break
                player = INITIAL_PLAYER
                reset_game(layout)

    window.close()


if __name__ == "__main__":
    main()