from time import sleep

SENTINEL = object()


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = SENTINEL

    @property
    def diameter(self):
        if self._diameter is SENTINEL:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self.radius * 2
        return self._diameter


circle = Circle(5)
print(circle.diameter)
