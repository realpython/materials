import functools
import importlib
import pathlib
import string


@functools.cache
def minimax(state, game, alpha=-2, beta=2, is_maximizing=True):
    if (score := game.evaluate(state, is_maximizing)) is not None:
        return score

    scores = []
    for new_state in game.possible_moves(state):
        scores.append(
            score := minimax(new_state, game, alpha, beta, not is_maximizing)
        )
        if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if is_maximizing else min)(scores)


def best_move(state, game):
    evaluate = functools.partial(minimax, game=game, is_maximizing=False)
    return max(game.possible_moves(state), key=evaluate, default=None)


def play_nim(game_name):
    game = import_game_engine(game_name)
    state = game.initial_state()

    while True:
        # Your move
        print(f"\nCurrent game: {state}")
        state = input_choice(game.possible_moves(state))
        if (score := game.evaluate(state, is_maximizing=False)) is not None:
            return game_over(score)

        # Minimax move
        new_state = best_move(state, game)
        print(f"\nI move from {state} to {new_state}")
        state = new_state
        if (score := game.evaluate(state, is_maximizing=True)) is not None:
            return game_over(score)


def game_over(score):
    print("You win! Well done!" if score > 0 else "I win! Try again!")


def import_game_engine(game_name):
    """Import the game engine to use"""
    return importlib.import_module(f"game_{game_name}")


def input_choice(choices, text="Please choose: "):
    inputs = dict(zip(string.ascii_letters, choices))
    for letter, choice in inputs.items():
        print(f"{letter}) {str(choice).replace('_', ' ').title()}")

    while (choice := input(text)) not in inputs:
        print(f"Choose one of {', '.join(inputs)}")

    return inputs[choice]


if __name__ == "__main__":
    game_engines = sorted(
        path.stem.removeprefix("game_")
        for path in sorted(pathlib.Path(__file__).parent.glob("game_*.py"))
    )
    game_name = input_choice(game_engines, "Choose a game: ")
    play_nim(game_name)
