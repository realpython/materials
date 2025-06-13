class Ball:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


class PoolBall(Ball):
    def __init__(self, color, number):
        super().__init__(color, shape="sphere")
        self.number = number


class AmericanFootBall(Ball):
    def __init__(self, color):
        super().__init__(color, shape="prolate spheroid")
