from abc import ABC

isinstance(eight_ball, ABC)

isinstance(football, ABC)

from collections.abc import Callable

isinstance(isinstance, Callable)

from balls import PoolBall

eight_ball = PoolBall("black", 8)

isinstance(eight_ball.get_shape, Callable)

isinstance(PoolBall, Callable)
