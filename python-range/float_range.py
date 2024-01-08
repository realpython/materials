from dataclasses import dataclass, field
from math import ceil, isclose


@dataclass
class FloatRange:
    """Range of numbers that allows floating point numbers."""

    start: float | int
    stop: float | int | None = None
    step: float | int = 1.0

    def __post_init__(self):
        """Validate parameters."""
        # Only one argument is given
        if self.stop is None:
            self.stop = self.start
            self.start = 0

        # Validate that all arguments are ints or floats
        if not isinstance(self.start, float | int):
            raise ValueError("'start' must be a floating point number")
        if not isinstance(self.stop, float | int):
            raise ValueError("'stop' must be a floating point number")
        if not isinstance(self.step, float | int) or isclose(self.step, 0):
            raise ValueError("'step' must be a non-zero floating point number")

    def __iter__(self):
        """Create an iterator based on the range."""
        return _FloatRangeIterator(self.start, self.stop, self.step)

    def __contains__(self, element):
        """Check if element is a member of the range.

        Use isclose() to handle floats.
        """
        offset = (element - self.start) % self.step
        if self.step > 0:
            return self.start <= element < self.stop and (
                isclose(offset, 0) or isclose(offset, self.step)
            )
        else:
            return self.stop < element <= self.start and (
                isclose(offset, 0) or isclose(offset, self.step)
            )

    def __len__(self):
        """Calculate the number of elements in the range."""
        if any(
            [
                self.step > 0 and self.stop <= self.start,
                self.step < 0 and self.stop >= self.start,
            ]
        ):
            return 0
        return ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        """Get an element in the range based on its index."""
        if index < 0 or index >= len(self):
            raise IndexError(f"range index out of range: {index}")
        return self.start + index * self.step

    def __reversed__(self):
        """Create a FloatRange with elements in the reverse order.

        Any number 0 < x < self.step can be used as offset. Use 0.1 when
        possible as an "esthetically nice" offset.
        """
        cls = type(self)
        offset = (1 if self.step > 0 else -1) * min(0.1, abs(self.step) / 2)
        return cls(
            (self.stop - self.step) + (self.start - self.stop) % self.step,
            self.start - offset,
            -self.step,
        )

    def count(self, element):
        """Count number of occurences of element in range."""
        return 1 if element in self else 0

    def index(self, element):
        """Calculate index of element in range."""
        if element not in self:
            raise ValueError(f"{element} is not in range")
        return round((element - self.start) / self.step)


@dataclass
class _FloatRangeIterator:
    """Non-public iterator. Should only be initialized by FloatRange."""

    start: float | int
    stop: float | int
    step: float | int
    _num_steps: int = field(default=0, init=False)

    def __iter__(self):
        """Initialize the iterator."""
        return self

    def __next__(self):
        """Calculate the next element in the iteration."""
        element = self.start + self._num_steps * self.step
        if any(
            [
                self.step > 0 and element >= self.stop,
                self.step < 0 and element <= self.stop,
            ]
        ):
            raise StopIteration
        self._num_steps += 1
        return element
