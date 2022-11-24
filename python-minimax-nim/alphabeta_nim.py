from functools import cache


@cache
def minimax(state, is_maximizing, alpha=-1, beta=1):
    if (score := evaluate(state, is_maximizing)) is not None:
        return score

    scores = []
    for new_state in possible_new_states(state):
        scores.append(
            score := minimax(new_state, not is_maximizing, alpha, beta)
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
        for new_state in possible_new_states(state)
    )


def possible_new_states(state):
    for pile, counters in enumerate(state):
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile + 1 :]


def evaluate(state, is_maximizing):
    if all(counters == 0 for counters in state):
        return 1 if is_maximizing else -1
