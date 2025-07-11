from abc import ABC
from collections.abc import Callable

from balls_v2 import AmericanFootBall, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")

# a)

isinstance(eight_ball, ABC)
isinstance(football, ABC)

# b)

isinstance(isinstance, Callable)
isinstance(PoolBall, Callable)

# c)

isinstance(eight_ball.get_state, Callable)

isinstance(PoolBall, Callable)
