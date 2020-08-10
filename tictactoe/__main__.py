from tictactoe.game import Game
from tictactoe.player import ConsolePlayer
from tictactoe.io import ConsoleFrontend, TableConsoleFrontend


def main():
    frontend = ConsoleFrontend()
    table_frontend = TableConsoleFrontend()
    player = ConsolePlayer("Real Python")
    game = Game(x_player=player, frontend=frontend)
    game.play()


if __name__ == "__main__":
    main()
