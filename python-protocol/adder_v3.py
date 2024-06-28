from typing import Protocol


class Adder(Protocol):
    def add(self, x: int | float, y: int | float) -> int | float: ...


class IntAdder:
    def add(self, x: int, y: int) -> int:
        return x + y


def add(adder: Adder) -> None:
    print(adder.add(2, 3))


# add(IntAdder())
