from balls import Ball, FootBall, PoolBall

football = FootBall("brown")
ball = Ball("green", "sphere")


isinstance(football, FootBall)

isinstance(football, PoolBall)

isinstance(ball, Ball)

isinstance(ball, FootBall)

isinstance(football, Ball)

isinstance(ball, PoolBall)

isinstance(1, bool)

isinstance(0, bool)
