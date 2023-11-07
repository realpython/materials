import numpy as np


def compute_cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Compute the cosine similarity between two vectors"""

    return u.dot(v) / (np.linalg.norm(u) * np.linalg.norm(v))
