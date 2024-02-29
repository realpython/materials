class Distance:
    _multiples = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1_000,
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit.lower()

    def to_meter(self):
        return self.value * type(self)._multiples[self.unit]

    def __add__(self, other):
        return self._compute(other, "+")

    def __sub__(self, other):
        return self._compute(other, "-")

    def _compute(self, other, operator):
        operation = eval(f"{self.to_meter()} {operator} {other.to_meter()}")
        cls = type(self)
        return cls(operation / cls._multiples[self.unit], self.unit)

    def __radd__(self, other):
        return self + other

    def __str__(self):
        return str(self.value) + self.unit

    def __repr__(self):
        return f"{type(self).__name__}(value={self.value}, unit={self.unit})"
