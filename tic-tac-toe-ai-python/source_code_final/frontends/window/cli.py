from queue import Queue
from threading import Thread

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import MinimaxComputerPlayer
from tic_tac_toe.logic.models import Mark

from .players import WindowPlayer
from .renderers import Window, WindowRenderer


def main() -> None:
    events: Queue = Queue()
    window = Window(events)
    Thread(target=game_loop, args=(window, events), daemon=True).start()
    window.mainloop()


def game_loop(window: Window, events: Queue) -> None:
    player1 = WindowPlayer(Mark("X"), events)
    player2 = MinimaxComputerPlayer(Mark("O"))
    starting_mark = Mark("X")
    TicTacToe(player1, player2, WindowRenderer(window)).play(starting_mark)
