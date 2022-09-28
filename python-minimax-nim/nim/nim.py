import functools
import importlib
import pathlib
import string


@functools.cache
def minimax(state, game, is_maximizing, alpha=-1, beta=1):
    """Evaluate a game state using the minimax algorithm"""
    if (score := game.evaluate(state, is_maximizing)) is not None:
        return score

    scores = []
    for new_state in game.possible_new_states(state):
        scores.append(
            score := minimax(new_state, game, not is_maximizing, alpha, beta)
        )
        if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if is_maximizing else min)(scores)


def best_move(state, game):
    """Use minimax() to find the best move"""
    evaluate = functools.partial(minimax, game=game, is_maximizing=False)
    return max(game.possible_new_states(state), key=evaluate, default=None)


def play_nim(game_name):
    """Main game loop"""
    game = import_game_engine(game_name)
    state = game.initial_state()

    while True:
        # Your move
        print(f"\nCurrent game: {state}")
        state = input_choice(game.possible_new_states(state))
        if (score := game.evaluate(state, is_maximizing=False)) is not None:
            return game_over(score)

        # Minimax move
        new_state = best_move(state, game)
        print(f"\nI move from {state} to {new_state}")
        state = new_state
        if (score := game.evaluate(state, is_maximizing=True)) is not None:
            return game_over(score)


def game_over(score):
    """Report on the result of the game"""
    print("You win! Well done!" if score > 0 else "I win! Try again!")


def import_game_engine(game_name):
    """Import the game engine to use"""
    return importlib.import_module(f"game_{game_name}")


def input_choice(choices, text="Please choose: "):
    """Get input from the player"""
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
