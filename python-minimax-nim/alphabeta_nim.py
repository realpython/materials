def minimax(state, alpha=-1, beta=1, is_maximizing=True):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score

    scores = []
    for new_state in possible_moves(state):
        scores.append(
            score := minimax(new_state, alpha, beta, not is_maximizing)
        )
        if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if is_maximizing else min)(scores)


def best_move(state):
    return max(
        (minimax(new_state, is_maximizing=False), new_state)
        for new_state in possible_moves(state)
    )


def evaluate(state, is_maximizing):
    if any(state):
        return None
    return 1 if is_maximizing else -1


def possible_moves(state):
    for pile, counters in enumerate(state):
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile + 1 :]
