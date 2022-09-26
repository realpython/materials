def minimax(state, is_maximizing=True):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score

    return (max if is_maximizing else min)(
        minimax(new_state, is_maximizing=not is_maximizing)
        for new_state in possible_moves(state)
    )


def best_move(state):
    return max(
        (minimax(new_state, is_maximizing=False), new_state)
        for new_state in possible_moves(state)
    )


def possible_moves(state):
    for pile, counters in enumerate(state):
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile + 1 :]


def evaluate(state, is_maximizing):
    if any(state):
        return None
    return 1 if is_maximizing else -1
