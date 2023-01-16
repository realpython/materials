import random


def initial_state():
    return (random.randint(6, 18),)


def possible_new_states(state):
    for pile, counters in enumerate(state):
        for take in range(1, (counters + 1) // 2):
            yield state[:pile] + (counters - take, take) + state[pile + 1 :]


def evaluate(state, is_maximizing):
    if all(counters <= 2 for counters in state):
        return -1 if is_maximizing else 1
