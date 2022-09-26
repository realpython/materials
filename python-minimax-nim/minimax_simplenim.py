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
    return [state - move for move in (1, 2, 3) if move <= state]


def evaluate(state, is_maximizing):
    if state > 0:
        return None
    return 1 if is_maximizing else -1
