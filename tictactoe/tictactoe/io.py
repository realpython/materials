from abc import ABC, abstractmethod
from tictactoe import Cell

import click
from terminaltables import SingleTable


class IOFrontend(ABC):
    @abstractmethod
    def print_board(self, board):
        pass

    @abstractmethod
    def print_winner(self, name=None):
        pass

    @abstractmethod
    def get_input(self):
        pass


class ConsoleFrontend(IOFrontend):
    def print_board(self, board):
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if (cell := board[i][j]) != Cell.EMPTY:
                    print(cell.value, end="|")
                else:
                    cell_number = i * len(row) + j + 1
                    print(cell_number, end="|")
            print()
        print()

    def print_winner(self, name=None):
        if name is None:
            print("Game is a draw!")
        else:
            print(f"Player {name} wins!")

    def get_input(self):
        return input("Enter a number of the cell: ")


class TableConsoleFrontend(IOFrontend):
    def print_board(self, board):
        table_data = []
        click.clear()
        for i, row in enumerate(board):
            table_row = []
            for j, column in enumerate(row):
                if (cell := board[i][j]) != Cell.EMPTY:
                    text = click.style(cell.value, fg="red", bold=True)
                    color = "red" if cell == Cell.X else "blue"
                    text = click.style(cell.value, fg=color, bold=True)
                else:
                    text = str(i * len(row) + j + 1)
                table_row.append(text)
            table_data.append(table_row)
        table = SingleTable(table_data=table_data)
        table.outer_border = False
        table.inner_row_border = True
        print(table.table)
        print()

    def print_winner(self, name=None):
        if name is not None:
            click.secho(f"{name} is a winner!", fg="black", bg="green")
        else:
            click.secho("A draw on the board!", fg="black", bg="cyan")

    def get_input(self):
        return input("Enter a number of the cell: ")
