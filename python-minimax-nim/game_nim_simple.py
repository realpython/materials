import random


def initial_state():
    return random.randint(10, 25)


def evaluate(state, is_maximizing):
    if state > 0:
        return None
    return 1 if is_maximizing else -1


def possible_moves(state):
    return [state - move for move in (1, 2, 3) if move <= state]
