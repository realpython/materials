import numpy as np
import pytest
from digitar.processing import normalize, remove_dc


@pytest.fixture
def audio_samples():
    return np.array([-5.0, -4.0, 1.0, 2.0])


def test_remove_dc(audio_samples):
    processed = remove_dc(audio_samples)
    assert processed is not audio_samples
    assert processed.tolist() == [-3.5, -2.5, 2.5, 3.5]


def test_normalize(audio_samples):
    processed = normalize(audio_samples)
    assert processed is not audio_samples
    assert processed.tolist() == [-1.0, -0.8, 0.2, 0.4]
