import dataclasses
from itertools import cycle
from math import sqrt

import pytest
from digitar.burst import SineWave, WhiteNoise


@pytest.fixture
def sampling_rate():
    return 44100


@pytest.fixture
def num_samples():
    return 1013


@pytest.fixture
def white_noise():
    return WhiteNoise()


@pytest.fixture
def sine_wave():
    return SineWave(frequency=440.2)


@pytest.fixture
def white_noise_samples(white_noise, num_samples, sampling_rate):
    return white_noise(num_samples, sampling_rate)


@pytest.fixture
def sine_wave_samples(sine_wave, num_samples, sampling_rate):
    return sine_wave(num_samples, sampling_rate)


@pytest.mark.parametrize(
    "fixture",
    [
        "white_noise_samples",
        "sine_wave_samples",
    ],
)
def test_should_have_specified_length(fixture, request, num_samples):
    audio_samples = request.getfixturevalue(fixture)
    assert audio_samples.shape == (num_samples,)


@pytest.mark.parametrize(
    "fixture",
    [
        "white_noise_samples",
        "sine_wave_samples",
    ],
)
def test_should_be_bound_to_value_range(fixture, request):
    audio_samples = request.getfixturevalue(fixture)
    assert audio_samples.max() <= 1.0
    assert audio_samples.min() >= -1.0


def test_white_noise_should_have_uniform_distribution(white_noise_samples):
    assert white_noise_samples.mean() == pytest.approx(0.0, abs=0.1)
    assert white_noise_samples.std() == pytest.approx(2 / sqrt(12), abs=0.1)


def test_sine_wave_should_have_correct_frequency(
    sine_wave, sine_wave_samples, sampling_rate
):
    sine_wave_period_seconds = 1.0 / sine_wave.frequency
    sine_wave_period_samples = sine_wave_period_seconds * sampling_rate
    quarter_samples = sine_wave_period_samples / 4
    value = cycle([0, 1, 0, -1])
    t = 0
    while t < len(sine_wave_samples):
        assert sine_wave_samples[round(t)] == pytest.approx(
            next(value), abs=0.1
        )
        t += quarter_samples


def test_sine_wave_should_be_immutable(sine_wave):
    with pytest.raises(dataclasses.FrozenInstanceError):
        sine_wave.frequency = 220.1
