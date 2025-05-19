from abc import ABC, abstractmethod


class Ball(ABC):
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    @abstractmethod
    def get_shape(self):
        pass


class PoolBall(Ball):
    def __init__(self, color, number):
        super().__init__(color, shape="sphere")
        self.number = number

    def get_shape(self):
        return self.shape


class AmericanFootBall(Ball):
    def __init__(self, color):
        super().__init__(color, shape="elongated ellipsoid")

    def get_shape(self):
        return "Elongated Ellipsoid"
