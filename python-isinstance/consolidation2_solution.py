from abc import ABC
from collections.abc import Callable

from balls_v2 import AmericanFootBall, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")

# 1.
print(f"{isinstance(eight_ball, ABC) = }")
print(f"{isinstance(football, ABC) = }")

# 2.
print()
print(f"{isinstance(isinstance, Callable) = }")
print(f"{isinstance(PoolBall, Callable) = }")

# 3.
print()
print(f"{isinstance(eight_ball.get_state, Callable) = }")
print(f"{isinstance(PoolBall, Callable) = }")
