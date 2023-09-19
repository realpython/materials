"""
Split in multiple dimensions.
"""

from dataclasses import dataclass
from functools import cached_property
from itertools import combinations_with_replacement, product, starmap
from math import floor, prod, sqrt
from typing import Iterator


@dataclass
class Bounds:
    """Spatial bounds defined in multiple dimensions."""

    start_point: tuple[int, ...]
    end_point: tuple[int, ...]

    def __post_init__(self) -> None:
        """Validate the bounds."""
        assert len(self.start_point) == len(self.end_point)
        assert self.start_point < self.end_point

    def __len__(self):
        """Get the number of points in the bounds (length, area, or volume).

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> len(bounds)
        7500
        """
        return prod(
            map(lambda x: x[1] - x[0], zip(self.start_point, self.end_point))
        )

    def __iter__(self) -> Iterator[tuple[int, ...]]:
        """Iterate over the bounds, yielding each point like in an odometer.

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> for x, y in bounds:
        ...     print(x, y)  # doctest: +ELLIPSIS
        50 25
        50 26
        50 27
        ...
        149 97
        149 98
        149 99
        """
        return product(*starmap(range, zip(self.start_point, self.end_point)))

    def slices(self) -> tuple[slice, ...]:
        """Return the slice for each dimension.

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> bounds.slices()
        (slice(50, 150, None), slice(25, 100, None))
        """
        return tuple(
            slice(start, end)
            for start, end in zip(self.start_point, self.end_point)
        )

    @cached_property
    def size(self) -> tuple[int, ...]:
        """Return the size of the bounds in each dimension.

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> width, height = bounds.size
        >>> width
        100
        >>> height
        75
        """
        return tuple(
            self.end_point[i] - self.start_point[i]
            for i in range(self.num_dimensions)
        )

    @cached_property
    def num_dimensions(self) -> int:
        """Return the number of dimensions.

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> bounds.num_dimensions
        2
        """
        return len(self.start_point)

    def offset(self, *coordinates):
        """Return the offset of the given coordinates from the start point.

        Example:
        >>> bounds = Bounds((50, 25), (150, 100))
        >>> for x, y in bounds:
        ...     print(bounds.offset(x, y))  # doctest: +ELLIPSIS
        (0, 0)
        (0, 1)
        (0, 2)
        ...
        (99, 72)
        (99, 73)
        (99, 74)
        """
        return tuple(
            coordinates[i] - self.start_point[i]
            for i in range(self.num_dimensions)
        )


def split_multi(num_chunks: int, *dimensions: int) -> Iterator[Bounds]:
    """Return a sequence of n-dimensional slices."""
    num_chunks_along_axis = find_most_even(num_chunks, len(dimensions))
    for slices_by_dimension in product(
        *starmap(get_slices, zip(dimensions, num_chunks_along_axis))
    ):
        yield Bounds(
            start_point=tuple(s.start for s in slices_by_dimension),
            end_point=tuple(s.stop for s in slices_by_dimension),
        )


def get_slices(length: int, num_chunks: int) -> Iterator[slice]:
    """Return a sequence of slices for the given length."""
    chunk_size, remaining = divmod(length, num_chunks)
    for i in range(num_chunks):
        begin = i * chunk_size + min(i, remaining)
        end = (i + 1) * chunk_size + min(i + 1, remaining)
        yield slice(begin, end)


def find_most_even(number: int, num_factors: int):
    """Return the most even tuple of integer divisors of a number."""
    products_by_sum = {
        sum(products): products
        for products in find_products(number, num_factors)
    }
    return products_by_sum[min(products_by_sum)]


def find_products(number: int, num_factors: int) -> Iterator[tuple[int, ...]]:
    """Return all possible products of a number."""
    divisors = find_divisors(number)
    for factors in combinations_with_replacement(divisors, num_factors):
        if prod(factors) == number:
            yield factors


def find_divisors(number: int) -> set[int]:
    """Return unique integer divisors of a number."""
    divisors = {1, number}
    for divisor in range(2, floor(sqrt(number)) + 1):
        factor, remainder = divmod(number, divisor)
        if remainder == 0:
            divisors.add(divisor)
            divisors.add(factor)
    return divisors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
