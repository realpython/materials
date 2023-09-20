from typing import TypeAlias, TypeVar

T = TypeVar("T")

Ordered: TypeAlias = list[T] | tuple[T, ...]

numbers: Ordered[int] = (1, 2, 3)


# %% Python 3.12

# type Ordered[T] = list[T] | tuple[T, ...]
#
# numbers: Ordered[int] = (1, 2, 3)
