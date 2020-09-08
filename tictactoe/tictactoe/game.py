from typing import Optional

from tictactoe import Cell
from tictactoe.player import Turn, RandomPlayer


class Game(object):
    def __init__(self, x_player=None, o_player=None, frontend=None):
        self.board = [
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
            [Cell.EMPTY, Cell.EMPTY, Cell.EMPTY],
        ]
        self.is_x_turn = True
        self.x_player = x_player or RandomPlayer()
        self.o_player = o_player or RandomPlayer()
        self.frontend = frontend

    def _check_draw(self) -> bool:
        for row in self.board:
            for cell in row:
                if cell == Cell.EMPTY:
                    return False
        return True

    def _check_winning_set(self, iterable) -> bool:
        unique = set(iterable)
        return Cell.EMPTY not in unique and len(unique) == 1

    def _check_winner(self) -> Optional[Cell]:
        # Check rows
        for row in self.board:
            if self._check_winning_set(row):
                return row[0]

        # Check columns
        for column in [*zip(*self.board)]:
            if self._check_winning_set(column):
                return column[0]

        # Check major diagonal
        size = len(self.board)
        major_diagonal = [self.board[i][i] for i in range(size)]
        if self._check_winning_set(major_diagonal):
            return major_diagonal[0]

        # Check minor diagonal
        minor_diagonal = [self.board[i][size - i - 1] for i in range(size)]
        if self._check_winning_set(minor_diagonal):
            return minor_diagonal[0]

    def is_game_over(self):
        winner = self._check_winner()
        if winner is not None:
            return winner

        return self._check_draw()

    def make_turn(self, turn: Turn, piece: Cell):
        self.board[turn.row][turn.column] = piece
        self.is_x_turn = not self.is_x_turn

    def print_board(self):
        self.frontend.print_board(self.board)

    def print_winner(self, winner):
        if winner == Cell.X:
            self.frontend.print_winner(self.x_player.name)
        elif winner == Cell.O:
            self.frontend.print_winner(self.o_player.name)
        else:
            self.frontend.print_winner()

    def play(self):
        self.print_board()
        while not (winner := self.is_game_over()):
            if self.is_x_turn:
                turn = self.x_player.get_turn(self.board)
                piece = Cell.X
            else:
                turn = self.o_player.get_turn(self.board)
                piece = Cell.O
            self.make_turn(turn, piece)
            self.print_board()
        self.print_winner(winner)
