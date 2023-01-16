import json
from functools import cache, partial
from importlib import resources

from tic_tac_toe.logic.models import GameState, Grid, Mark, Move


class MinimaxSerializer:
    DEFAULT_FILENAME = "minimax.json"

    @staticmethod
    def key(move: Move) -> str:
        return move.before_state.grid.cells + move.after_state.grid.cells

    @staticmethod
    @cache
    def load(filename: str = DEFAULT_FILENAME) -> dict:
        with resources.open_text(__package__, filename) as file:
            return json.load(file)

    @staticmethod
    def dump(filename: str = DEFAULT_FILENAME) -> None:
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump(MinimaxSerializer.precompute_scores(), file)

    @staticmethod
    def precompute_scores() -> dict[str, list[int]]:
        scores = {}

        def traverse(game_state: GameState) -> None:
            for move in game_state.possible_moves:
                scores[MinimaxSerializer.key(move)] = [
                    minimax(move, Mark("X")),
                    minimax(move, Mark("O")),
                ]
                traverse(move.after_state)

        traverse(GameState(Grid(), Mark("X")))
        traverse(GameState(Grid(), Mark("O")))

        return scores


def find_best_move(game_state: GameState) -> Move | None:
    maximizer: Mark = game_state.current_mark
    bound_minimax = partial(minimax, maximizer=maximizer)
    return max(game_state.possible_moves, key=bound_minimax)


def find_best_move_optimized(game_state: GameState) -> Move | None:
    maximizer: Mark = game_state.current_mark

    def alpha_beta(
        move: Move, alpha=-2, beta=2, choose_highest_score: bool = False
    ) -> int:
        if move.after_state.game_over:
            return move.after_state.evaluate_score(maximizer)

        if choose_highest_score:
            score = -2
            for next_move in move.after_state.possible_moves:
                evaluation = alpha_beta(next_move, alpha, beta, False)
                score = max(score, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return score
        else:
            score = 2
            for next_move in move.after_state.possible_moves:
                evaluation = alpha_beta(next_move, alpha, beta, True)
                score = min(score, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return score

    return max(game_state.possible_moves, key=alpha_beta)


def find_best_move_precomputed(game_state: GameState) -> Move | None:
    scores = MinimaxSerializer.load()
    maximizer: Mark = game_state.current_mark
    return max(
        game_state.possible_moves,
        key=lambda move: scores[MinimaxSerializer.key(move)][
            0 if maximizer == "X" else 1
        ],
    )


def minimax(
    move: Move, maximizer: Mark, choose_highest_score: bool = False
) -> int:
    if move.after_state.game_over:
        return move.after_state.evaluate_score(maximizer)
    return (max if choose_highest_score else min)(
        minimax(next_move, maximizer, not choose_highest_score)
        for next_move in move.after_state.possible_moves
    )
