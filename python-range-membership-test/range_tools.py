import math
from dataclasses import dataclass, field


@dataclass
class Range:
    start: int
    stop: int
    step: int = 1

    def __post_init__(self):
        """Validate parameters."""
        if not isinstance(self.start, int):
            raise ValueError("'start' must be an integer")
        if not isinstance(self.stop, int):
            raise ValueError("'stop' must be an integer")
        if not isinstance(self.step, int) or self.step <= 0:
            raise ValueError("'step' must be a positive integer")

    def __iter__(self):
        """Create an iterator based on the range."""
        return _RangeIterator(self.start, self.stop, self.step)

    def __contains__(self, element):
        """Check if element is a member of the range."""
        return (
            self.start <= element < self.stop
            and (element - self.start) % self.step == 0
        )

    def __len__(self):
        """Calculate the number of elements in the range."""
        if self.stop <= self.start:
            return 0
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        """Get an element in the range based on its index."""
        if index < 0 or index >= len(self):
            raise IndexError(f"range index out of range: {index}")
        return self.start + index * self.step

    def count(self, element):
        """Count number of occurences of element in range."""
        return 1 if element in self else 0

    def index(self, element):
        """Calculate index of element in range."""
        if element not in self:
            raise ValueError(f"{element} not in range")
        return (element - self.start) // self.step


@dataclass
class _RangeIterator:
    start: int
    stop: int
    step: int
    _state: int | None = field(default=None, init=False)

    def __next__(self):
        """Calculate the next element in the iteration."""
        if self._state is None:
            self._state = self.start
        else:
            self._state += self.step
        if self._state >= self.stop:
            raise StopIteration
        return self._state
