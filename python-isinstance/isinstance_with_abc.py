from balls_v2 import AmericanFootBall, Ball, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")

print(f"{isinstance(eight_ball, Ball) = }")
print(f"{isinstance(football, Ball) = }")
