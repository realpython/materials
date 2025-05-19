from abc import ABC
from collections.abc import Callable
from balls_v2 import AmericanFootBall, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")

isinstance(eight_ball, ABC)

isinstance(football, ABC)

isinstance(isinstance, Callable)

isinstance(eight_ball.get_shape, Callable)

isinstance(PoolBall, Callable)
