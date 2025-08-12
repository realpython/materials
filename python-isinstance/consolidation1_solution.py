from balls import AmericanFootBall, Ball, PoolBall

ball = Ball("green", "sphere")
football = AmericanFootBall("brown")

print(f"{isinstance(football, AmericanFootBall) = }")
print(f"{isinstance(football, PoolBall) = }")
print(f"{isinstance(ball, Ball) = }")
print(f"{isinstance(ball, AmericanFootBall) = }")
print(f"{isinstance(football, Ball) = }")
print(f"{isinstance(ball, PoolBall) = }")
print(f"{isinstance(1, bool) = }")
print(f"{isinstance(0, bool) = }")
