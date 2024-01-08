from dataclasses import dataclass


@dataclass
class PiDigits:
    num_digits: int

    def __index__(self):
        return int("3141592653589793238462643383279"[: self.num_digits])
