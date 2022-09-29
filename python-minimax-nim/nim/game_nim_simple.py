import random


def initial_state():
    return random.randint(10, 25)


def possible_new_states(state):
    return [state - take for take in (1, 2, 3) if take <= state]


def evaluate(state, is_maximizing):
    if state == 0:
        return 1 if is_maximizing else -1
