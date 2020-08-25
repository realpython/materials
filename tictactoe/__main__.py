from tictactoe.game import Game
from tictactoe.player import ConsolePlayer
from tictactoe.io import ConsoleFrontend


def main():
    frontend = ConsoleFrontend()
    player = ConsolePlayer("Real Python")
    game = Game(x_player=player, frontend=frontend)
    game.play()


if __name__ == "__main__":
    main()
