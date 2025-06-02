from balls import Ball, FootBall, PoolBall

ball = Ball("green", "sphere")
football = FootBall("brown")

isinstance(football, FootBall)

isinstance(football, PoolBall)

isinstance(ball, Ball)

isinstance(ball, FootBall)

isinstance(football, Ball)

isinstance(ball, PoolBall)

isinstance(1, bool)

isinstance(0, bool)
