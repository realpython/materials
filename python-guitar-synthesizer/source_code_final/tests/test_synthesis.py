import dataclasses

import pytest
from digitar.burst import SineWave, WhiteNoise
from digitar.chord import Chord
from digitar.instrument import PluckedStringInstrument, StringTuning
from digitar.stroke import Velocity
from digitar.synthesis import Synthesizer
from digitar.temporal import Time


@pytest.fixture
def instrument():
    return PluckedStringInstrument(
        tuning=StringTuning.from_notes("E1", "A1", "D2", "G2"),
        vibration=Time(seconds=2.5),
        damping=0.465,
    )


@pytest.fixture
def synthesizer(instrument):
    return Synthesizer(instrument)


@pytest.fixture
def chord():
    return Chord.from_numbers(0, None, 3, 0)


@pytest.fixture
def downstroke(instrument):
    return Velocity.down(Time.from_milliseconds(5))


def test_create_with_defaults(instrument):
    synthesizer = Synthesizer(instrument)
    assert synthesizer.instrument is instrument
    assert isinstance(synthesizer.burst_generator, WhiteNoise)
    assert synthesizer.sampling_rate == 44100


def test_create_with_custom_parameters(instrument):
    synthesizer = Synthesizer(instrument, SineWave(440), 22050)
    assert synthesizer.instrument is instrument
    assert isinstance(synthesizer.burst_generator, SineWave)
    assert synthesizer.sampling_rate == 22050


def test_synthesizer_should_be_immutable(synthesizer):
    with pytest.raises(dataclasses.FrozenInstanceError):
        synthesizer.sampling_rate = 22050
