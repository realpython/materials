from balls import AmericanFootBall, Ball, PoolBall

eight_ball = PoolBall("black", 8)
football = AmericanFootBall("brown")
ball = Ball("green", "sphere")

isinstance(eight_ball, PoolBall)
isinstance(eight_ball, Ball)
isinstance(eight_ball, AmericanFootBall)

isinstance(eight_ball, object)
isinstance(football, object)
isinstance(ball, object)
isinstance(object, object)
