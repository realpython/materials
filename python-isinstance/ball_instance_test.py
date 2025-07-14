from balls import AmericanFootBall, Ball, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")
ball = Ball("green", "sphere")

print(f"{isinstance(eight_ball, PoolBall) = }")
print(f"{isinstance(eight_ball, Ball) = }")
print(f"{isinstance(eight_ball, AmericanFootBall) = }")

print(f"{isinstance(eight_ball, object) = }")
print(f"{isinstance(football, object) = }")
print(f"{isinstance(ball, object) = }")
print(f"{isinstance(object, object) = }")
