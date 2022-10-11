import abc
import asyncio

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.minimax import find_best_move_precomputed
from tic_tac_toe.logic.models import GameState, Mark, Move


class AsyncPlayer(metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    async def make_move(self, game_state: GameState) -> GameState:
        if self.mark is game_state.current_mark:
            if move := await self.get_move(game_state):
                return move.after_state
            raise InvalidMove("No more possible moves")
        else:
            raise InvalidMove("It's the other player's turn")

    @abc.abstractmethod
    async def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""


class AsyncComputerPlayer(AsyncPlayer, metaclass=abc.ABCMeta):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25) -> None:
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    async def get_move(self, game_state: GameState) -> Move | None:
        await asyncio.sleep(self.delay_seconds)
        return await self.get_computer_move(game_state)

    @abc.abstractmethod
    async def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the computer's move in the given game state."""


class AsyncRandomComputerPlayer(AsyncComputerPlayer):
    async def get_computer_move(self, game_state: GameState) -> Move | None:
        return game_state.make_random_move()


class AsyncMinimaxComputerPlayer(AsyncComputerPlayer):
    async def get_computer_move(self, game_state: GameState) -> Move | None:
        if game_state.game_not_started:
            return game_state.make_random_move()
        else:
            return find_best_move_precomputed(game_state)
