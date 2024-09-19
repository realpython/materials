from functools import cache
from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    @cache
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2
