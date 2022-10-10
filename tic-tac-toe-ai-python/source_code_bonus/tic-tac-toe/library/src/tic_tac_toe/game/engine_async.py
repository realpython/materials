from dataclasses import dataclass

from tic_tac_toe.game.engine import ErrorHandler
from tic_tac_toe.game.players_async import AsyncPlayer
from tic_tac_toe.game.renderers import Renderer
from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import GameState, Grid, Mark
from tic_tac_toe.logic.validators import validate_players


@dataclass(frozen=True)
class AsyncTicTacToe:
    player1: AsyncPlayer
    player2: AsyncPlayer
    renderer: Renderer
    error_handler: ErrorHandler | None = None

    def __post_init__(self):
        validate_players(self.player1, self.player2)

    async def play(self, starting_mark: Mark = Mark("X")) -> None:
        game_state = GameState(Grid(), starting_mark)
        while True:
            self.renderer.render(game_state)
            if game_state.game_over:
                break
            player = self.get_current_player(game_state)
            try:
                game_state = await player.make_move(game_state)
            except InvalidMove as ex:
                if self.error_handler:
                    self.error_handler(ex)

    def get_current_player(self, game_state: GameState) -> AsyncPlayer:
        if game_state.current_mark is self.player1.mark:
            return self.player1
        else:
            return self.player2
