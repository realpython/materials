import random


def initial_state():
    return tuple(random.randint(3, 9) for _ in range(random.randint(3, 5)))


def evaluate(state, is_maximizing):
    if any(state):
        return None
    return -1 if is_maximizing else 1


def possible_moves(state):
    for pile, counters in enumerate(state):
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile + 1 :]
