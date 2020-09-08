import random
import string
from abc import ABC, abstractmethod
from random import choice
from dataclasses import dataclass

from tictactoe import Cell
from tictactoe.io import ConsoleFrontend


@dataclass
class Turn:
    row: int
    column: int


class Player(ABC):
    def __init__(self, name=None, frontend=None):
        self.name = name
        self.frontend = frontend

    @abstractmethod
    def get_turn(self, board):
        pass


class RandomPlayer(Player):
    def __init__(self):
        random_name = "".join(
            [random.choice(string.ascii_letters) for _ in range(8)]
        )
        super().__init__(name=random_name)

    def get_turn(self, board):
        available_turns = []
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if board[i][j] == Cell.EMPTY:
                    t = Turn(i, j)
                    available_turns.append(t)
        return choice(available_turns)


class ConsolePlayer(Player):
    def __init__(self, name="Console Player"):
        frontend = ConsoleFrontend()
        super().__init__(name=name, frontend=frontend)

    def get_turn(self, board):
        size = len(board)
        while True:
            index = int(self.frontend.get_input()) - 1
            row = index // size
            column = index % size
            return Turn(row, column)
