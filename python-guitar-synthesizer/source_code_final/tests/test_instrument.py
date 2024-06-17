import dataclasses

import pytest
from digitar.chord import Chord
from digitar.instrument import (
    PluckedStringInstrument,
    StringTuning,
    VibratingString,
)
from digitar.pitch import Pitch
from digitar.temporal import Time


@pytest.fixture
def pitch():
    return Pitch.from_scientific_notation("C")


@pytest.fixture
def vibrating_string(pitch):
    return VibratingString(pitch)


@pytest.fixture
def string_tuning():
    return StringTuning(
        strings=(
            VibratingString(pitch=Pitch(frequency=329.6275569128699)),
            VibratingString(pitch=Pitch(frequency=246.94165062806206)),
            VibratingString(pitch=Pitch(frequency=195.99771799087463)),
            VibratingString(pitch=Pitch(frequency=146.8323839587038)),
            VibratingString(pitch=Pitch(frequency=110.0000000000000)),
            VibratingString(pitch=Pitch(frequency=82.4068892282175)),
        )
    )


@pytest.fixture
def plucked_string_instrument(string_tuning):
    return PluckedStringInstrument(
        string_tuning, vibration=Time(4.5), damping=0.465
    )


def test_vibrating_string_get_pitch(pitch, vibrating_string):
    assert vibrating_string.pitch is pitch


def test_vibrating_string_press_open(vibrating_string):
    new_pitch = vibrating_string.press_fret()
    assert new_pitch is vibrating_string.pitch


def test_vibrating_string_press_fretted(vibrating_string):
    new_pitch = vibrating_string.press_fret(fret_number=10)
    assert new_pitch == vibrating_string.pitch.adjust(num_semitones=10)


def test_vibrating_string_should_be_immutable(vibrating_string):
    with pytest.raises(dataclasses.FrozenInstanceError):
        vibrating_string.pitch = Pitch.from_scientific_notation("D")


def test_string_tuning_create_from_notes():
    string_tuning = StringTuning.from_notes("E2", "A2", "D3", "G3", "B3", "E4")
    pitches = [string.pitch for string in string_tuning.strings]
    assert pitches == [
        Pitch.from_scientific_notation("E4"),
        Pitch.from_scientific_notation("B3"),
        Pitch.from_scientific_notation("G3"),
        Pitch.from_scientific_notation("D3"),
        Pitch.from_scientific_notation("A2"),
        Pitch.from_scientific_notation("E2"),
    ]


def test_string_tuning_get_strings(string_tuning):
    assert string_tuning.strings == (
        VibratingString(pitch=Pitch(frequency=329.6275569128699)),
        VibratingString(pitch=Pitch(frequency=246.94165062806206)),
        VibratingString(pitch=Pitch(frequency=195.99771799087463)),
        VibratingString(pitch=Pitch(frequency=146.8323839587038)),
        VibratingString(pitch=Pitch(frequency=110.0)),
        VibratingString(pitch=Pitch(frequency=82.4068892282175)),
    )


def test_string_tuning_should_be_immutable(string_tuning, vibrating_string):
    with pytest.raises(dataclasses.FrozenInstanceError):
        string_tuning.strings = (vibrating_string,)


@pytest.mark.parametrize(
    "damping",
    [
        -0.1,
        0.51,
    ],
)
def test_plucked_string_instrument_invalid_tension(damping, string_tuning):
    with pytest.raises(ValueError):
        PluckedStringInstrument(string_tuning, Time(1.5), damping)


def test_plucked_string_instrument_get_attributes(
    plucked_string_instrument, string_tuning
):
    assert plucked_string_instrument.tuning == string_tuning
    assert plucked_string_instrument.vibration == Time(4.5)
    assert plucked_string_instrument.damping == 0.465


def test_plucked_string_instrument_get_num_strings(
    plucked_string_instrument,
):
    assert plucked_string_instrument.num_strings == len(
        plucked_string_instrument.tuning.strings
    )


@pytest.mark.parametrize(
    "chord, pitches",
    [
        (Chord.from_numbers(None, None, None, None, None, None), ()),
        (
            Chord.from_numbers(0, 0, 0, 0, 0, 0),
            (
                Pitch.from_scientific_notation("E2"),
                Pitch.from_scientific_notation("A2"),
                Pitch.from_scientific_notation("D3"),
                Pitch.from_scientific_notation("G3"),
                Pitch.from_scientific_notation("B3"),
                Pitch.from_scientific_notation("E4"),
            ),
        ),
        (
            Chord.from_numbers(0, None, 1, 2, 3, 4),
            (
                Pitch.from_scientific_notation("E2").adjust(4),
                Pitch.from_scientific_notation("A2").adjust(3),
                Pitch.from_scientific_notation("D3").adjust(2),
                Pitch.from_scientific_notation("G3").adjust(1),
                Pitch.from_scientific_notation("E4"),
            ),
        ),
    ],
)
def test_plucked_string_instrument_downstroke(
    chord, pitches, plucked_string_instrument
):
    assert plucked_string_instrument.downstroke(chord) == pitches


@pytest.mark.parametrize(
    "chord, pitches",
    [
        (Chord.from_numbers(None, None, None, None, None, None), ()),
        (
            Chord.from_numbers(0, 0, 0, 0, 0, 0),
            (
                Pitch.from_scientific_notation("E4"),
                Pitch.from_scientific_notation("B3"),
                Pitch.from_scientific_notation("G3"),
                Pitch.from_scientific_notation("D3"),
                Pitch.from_scientific_notation("A2"),
                Pitch.from_scientific_notation("E2"),
            ),
        ),
        (
            Chord.from_numbers(0, None, 1, 2, 3, 4),
            (
                Pitch.from_scientific_notation("E4"),
                Pitch.from_scientific_notation("G3").adjust(1),
                Pitch.from_scientific_notation("D3").adjust(2),
                Pitch.from_scientific_notation("A2").adjust(3),
                Pitch.from_scientific_notation("E2").adjust(4),
            ),
        ),
    ],
)
def test_plucked_string_instrument_upstroke(
    chord, pitches, plucked_string_instrument
):
    assert plucked_string_instrument.upstroke(chord) == pitches


def test_plucked_string_instrument_downstroke_invalid_chord(
    plucked_string_instrument,
):
    with pytest.raises(ValueError):
        plucked_string_instrument.downstroke(Chord((1, 2, 3)))


def test_plucked_string_instrument_upstroke_invalid_chord(
    plucked_string_instrument,
):
    with pytest.raises(ValueError):
        plucked_string_instrument.upstroke(Chord((1, 2, 3)))


def test_plucked_string_instrument_should_be_immutable(
    plucked_string_instrument,
):
    with pytest.raises(dataclasses.FrozenInstanceError):
        plucked_string_instrument.string_tension = 0.5


def test_plucked_string_instrument_cache_downstroke(
    plucked_string_instrument,
):
    chord = Chord.from_numbers(0, None, 1, 2, 3, 4)
    result1 = plucked_string_instrument.downstroke(chord)
    result2 = plucked_string_instrument.downstroke(chord)
    assert result1 is result2


def test_plucked_string_instrument_cache_upstroke(
    plucked_string_instrument,
):
    chord = Chord.from_numbers(0, None, 1, 2, 3, 4)
    result1 = plucked_string_instrument.upstroke(chord)
    result2 = plucked_string_instrument.upstroke(chord)
    assert result1 is result2
