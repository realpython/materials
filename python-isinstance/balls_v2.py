from abc import ABC, abstractmethod


class Ball(ABC):
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    @abstractmethod
    def get_state(self):
        pass


class PoolBall(Ball):
    def __init__(self, color, number):
        super().__init__(color, shape="sphere")
        self.number = number

    def get_state(self):
        print(
            f"Color = {self.color}, Number = {self.number}, Shape = {self.shape}"
        )


class AmericanFootBall(Ball):
    def __init__(self, color):
        super().__init__(color, shape="prolate spheroid")

    def get_state(self):
        print(f"Color = {self.color}, Shape = {self.shape}")
