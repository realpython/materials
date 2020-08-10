import random
import string
from abc import ABC, abstractmethod
from random import choice

from tictactoe import Cell
from tictactoe.io import ConsoleFrontend


class Player(ABC):
    def __init__(self, name=None, frontend=None):
        self.name = name
        self.frontend = frontend

    @abstractmethod
    def get_turn(self, board) -> int:
        pass


class RandomPlayer(Player):
    def __init__(self):
        random_name = "".join(
            [random.choice(string.ascii_letters) for _ in range(8)]
        )
        super().__init__(name=random_name)

    def get_turn(self, board):
        available_cells = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if board[i][j] == Cell.EMPTY:
                    cell_index = i * len(board) + j
                    available_cells.append(cell_index)
        return choice(available_cells)


class ConsolePlayer(Player):
    def __init__(self, name="Console Player"):
        frontend = ConsoleFrontend()
        super().__init__(name=name, frontend=frontend)

    def get_turn(self, board) -> int:
        while True:
            index = self.frontend.get_input()
            return int(index) - 1
