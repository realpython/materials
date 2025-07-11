from balls import AmericanFootBall, Ball, PoolBall

ball = Ball("green", "sphere")
football = AmericanFootBall("brown")

isinstance(football, AmericanFootBall)

isinstance(football, PoolBall)

isinstance(ball, Ball)

isinstance(ball, AmericanFootBall)

isinstance(football, Ball)

isinstance(ball, PoolBall)

isinstance(1, bool)

isinstance(0, bool)
