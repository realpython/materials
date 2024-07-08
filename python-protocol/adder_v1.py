from typing import Protocol


class Adder(Protocol):
    def add(self, x, y): ...


class IntAdder:
    def add(self, x, y):
        return x + y


class FloatAdder:
    def add(self, x, y):
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


add(IntAdder())
add(FloatAdder())


for adder in [IntAdder(), FloatAdder()]:
    add(adder)
