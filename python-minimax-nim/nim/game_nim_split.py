import random


def initial_state():
    return (random.randint(6, 18),)


def evaluate(state, is_maximizing):
    if any(pile > 2 for pile in state):
        return None
    return -1 if is_maximizing else 1


def possible_moves(state):
    for pile, counters in enumerate(state):
        for take in range(1, (counters + 1) // 2):
            yield state[:pile] + (counters - take, take) + state[pile + 1 :]
