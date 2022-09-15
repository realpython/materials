from enum import Enum
from itertools import cycle


class Band(Enum):
    AM = ["1250", "1380", "1510"]
    FM = ["81.3", "89.1", "103.9"]


class Radio:
    def __init__(self, bands=Band):
        self._bands = cycle(bands)
        self.current_band = next(self._bands)
        self._pos = 0

    def toggle_band(self):
        self.current_band = next(self._bands)
        self._pos = 0

    def tune(self):
        self._pos += 1
        if self._pos == len(self.current_band.value):
            self._pos = 0
        print(
            "Tuning... Station is",
            f"{self.current_band.value[self._pos]} {self.current_band.name}",
        )


if __name__ == "__main__":
    radio = Radio()
    actions = (
        [radio.tune] * len(radio.current_band.value)
        + [radio.toggle_band]
        + [radio.tune] * len(radio.current_band.value)
    )
    for action in actions:
        action()
