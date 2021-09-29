import io
import random
from collections import namedtuple

import PySimpleGUI as sg
from PIL import Image

APP_NAME = "Tic-Tac-Toe"
BLANK_IMAGE_PATH = "assets/blank.png"
BOARD_SIZE = 3
BG_COLOR = "white"
HL_COLOR = "green"

Player = namedtuple("Player", "name image")
PLAYER_X = Player("X", "assets/x.png")
PLAYER_O = Player("O", "assets/o.png")


def main():
    """Create the game board and run the game loop."""
    game_board = build_game_board()
    try:
        game_loop(game_board)
    finally:
        game_board.close()


def build_game_board():
    """Return the game board."""
    board_grid = [
        [
            sg.Button(
                size=(7, 5),
                key=(row, col),
                button_color=(BG_COLOR, BG_COLOR),
                image_filename=BLANK_IMAGE_PATH,
            )
            for row in range(BOARD_SIZE)
        ]
        for col in range(BOARD_SIZE)
    ]
    game_board = sg.Window(APP_NAME, layout=board_grid)
    game_board.grid = board_grid
    game_board.winning_combos = _get_winning_combos(board_grid)
    return game_board


def _get_winning_combos(board_grid):
    horizontal = [
        [board_grid[y][x] for x in range(len(board_grid))]
        for y in range(len(board_grid))
    ]
    vertical = [
        [board_grid[y][x] for y in range(len(board_grid))]
        for x in range(len(board_grid))
    ]
    diagonal = [
        [board_grid[d][d] for d in range(len(board_grid))],
        [board_grid[-1 - d][d] for d in range(len(board_grid))],
    ]
    return horizontal + vertical + diagonal


def game_loop(game_board):
    """Implement the game loop."""
    player = random.choice((PLAYER_X, PLAYER_O))  # Initial player

    while True:
        event, _ = game_board.read()
        # 1. If it's a close event
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # 2. If it's not a player movement (Not a button click event)
        if not isinstance(event, tuple):
            continue

        # 3. If it's a player movement (Button click event)
        clicked_cell = game_board[event]
        # If cell was already clicked, continue
        if clicked_cell.metadata is not None:
            continue

        update_board_cell(player, clicked_cell)
        winner, winning_combo = confirm_winning_condition(
            player, game_board.winning_combos
        )

        # If there's a winning condition or a tied game
        if winner or is_tied_game(game_board):
            if winner:
                highlight_cells(winning_combo)
            if play_again(winner):
                reset_game_board(game_board)
                continue
            else:
                break

        player = toggle_player(player)


def update_board_cell(player, clicked_cell):
    """Update the game board."""
    image = _get_image_stream(file_path=player.image)
    clicked_cell.update(image_data=image)
    clicked_cell.metadata = player.name


def _get_image_stream(file_path):
    bio = io.BytesIO()
    image = Image.open(file_path)
    image.save(bio, format="PNG")
    return bio.getvalue()


def confirm_winning_condition(player, winning_combos):
    """Return the winner and the winning combination, if any."""
    for combo in winning_combos:
        results = {cell.metadata for cell in combo}
        is_won = (len(results) == 1) and (None not in results)
        if is_won:
            return player, combo
    return None, None


def is_tied_game(board):
    """Return True if the game is tied, `False` otherwise."""
    # If all the cells were clicked without a winner
    all_clicked = all(cell.metadata for row in board.grid for cell in row)
    return all_clicked


def highlight_cells(cells):
    """Highlight the winning cells with a different background color."""
    for cell in cells:
        cell.update(button_color=(HL_COLOR, HL_COLOR))


def play_again(player):
    """Display the game's result and ask if play again or quit."""
    if player is None:
        message = "Tied Game!"
    else:
        message = f'Player "{player.name}" won!'
    quit_dialog_layout = [
        [sg.Text(f"{message} Do you want to play again?")],
        [sg.Button("Play"), sg.Button("Quit")],
    ]
    quit_dialog = sg.Window(APP_NAME, quit_dialog_layout, modal=True)
    event, _ = quit_dialog.read(close=True)
    return event == "Play"


def reset_game_board(board):
    """Reset the game board to start a new game."""
    image = _get_image_stream(BLANK_IMAGE_PATH)
    for row in board.grid:
        for cell in row:
            cell.update(image_data=image, button_color=(BG_COLOR, BG_COLOR))
            cell.metadata = None


def toggle_player(player):
    """Toggle the current player."""
    if player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X


if __name__ == "__main__":
    main()
