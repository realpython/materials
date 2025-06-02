from abc import ABC
from collections.abc import Callable

from balls_v2 import AmericanFootBall, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")

# Question 1

isinstance(eight_ball, ABC)
isinstance(football, ABC)

# Question 2

isinstance(isinstance, Callable)

# Question 3

isinstance(eight_ball.get_shape, Callable)

isinstance(PoolBall, Callable)
