import numpy as np


def remove_dc(samples: np.ndarray) -> np.ndarray:
    return samples - samples.mean()


def normalize(samples: np.ndarray) -> np.ndarray:
    return samples / np.abs(samples).max()
