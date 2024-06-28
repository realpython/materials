from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    return float(a + b)


print(add(2, 4))
# print(add("2", "4"))
