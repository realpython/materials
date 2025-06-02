from balls import Ball, FootBall, PoolBall

eight_ball = PoolBall("black", 8)
football = FootBall("brown")
ball = Ball("green", "sphere")

isinstance(eight_ball, PoolBall)
isinstance(eight_ball, Ball)
isinstance(eight_ball, FootBall)

isinstance(eight_ball, object)
isinstance(football, object)
isinstance(ball, object)
isinstance(object, object)
