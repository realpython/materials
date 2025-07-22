from balls import Ball, PoolBall

eight_ball = PoolBall("black", 8)

print(f"{type(eight_ball) = }")
print(f"{type(eight_ball) is PoolBall = }")
print(f"{isinstance(eight_ball, Ball) = }")
print(f"{type(eight_ball) is Ball = }")
