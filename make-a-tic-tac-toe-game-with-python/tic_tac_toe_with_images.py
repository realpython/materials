import io
import PySimpleGUI as sg

from PIL import Image


PLAYER_X_IMAGE_PATH = "assets/X.png"
PLAYER_O_IMAGE_PATH = "assets/O.png"
BLANK_IMAGE_PATH = "assets/BLANK.png"


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
    layout = [
        [
            sg.Button(
                size=(10, 6),
                key=(row, col),
                button_color=("white", "white"),
                image_filename=BLANK_IMAGE_PATH,
            )
            for row in range(3)
        ]
        for col in range(3)
    ]
    window = sg.Window("Tic-Tac-Toe", layout)

    player = "X"
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if isinstance(event, tuple):
            btn_clicked = window[event]
            player = update_game(btn_clicked, player)

    window.close()


if __name__ == "__main__":
    main()