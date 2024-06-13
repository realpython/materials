from typing import Protocol

import numpy as np

from digitar.temporal import Hertz


class BurstGenerator(Protocol):
    def __call__(
        self, num_samples: int, sampling_rate: Hertz
    ) -> np.ndarray: ...


class WhiteNoise:
    def __call__(self, num_samples: int, sampling_rate: Hertz) -> np.ndarray:
        return np.random.uniform(-1.0, 1.0, num_samples)
