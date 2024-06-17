import dataclasses

import pytest
from digitar.pitch import Pitch


def test_should_create_from_hertz():
    hertz = 16.351597831287414
    pitch = Pitch(hertz)
    assert pitch.frequency == hertz


@pytest.mark.parametrize(
    "note, hertz",
    [
        ("C", 16.351597831287414),
        ("C#", 17.323914436054505),
        ("D", 18.354047994837977),
        ("D#", 19.445436482630058),
        ("E", 20.601722307054366),
        ("F", 21.826764464562746),
        ("F#", 23.12465141947715),
        ("G", 24.499714748859326),
        ("G#", 25.956543598746574),
        ("A", 27.5),
        ("A#", 29.13523509488062),
        ("B", 30.86770632850775),
    ],
)
def test_should_create_from_scientific_notation(note, hertz):
    pitch = Pitch.from_scientific_notation(note)
    assert pitch.frequency == hertz


def test_should_reject_invalid_notation():
    with pytest.raises(ValueError):
        Pitch.from_scientific_notation("E#")


@pytest.mark.parametrize(
    "note, hertz",
    [
        ("C-10", 0.015968357257116615),
        ("C-2", 4.0878994578218535),
        ("C-1", 8.175798915643707),
        ("C0", 16.351597831287414),
        ("C1", 32.70319566257483),
        ("C2", 65.40639132514966),
        ("C10", 16744.036179238312),
        ("C#-10", 0.016917885191459484),
        ("C#-2", 4.330978609013626),
        ("C#-1", 8.661957218027252),
        ("C#0", 17.323914436054505),
        ("C#1", 34.64782887210901),
        ("C#2", 69.29565774421802),
        ("C#10", 17739.688382519813),
    ],
)
def test_should_change_octave(note, hertz):
    pitch = Pitch.from_scientific_notation(note)
    assert pitch.frequency == hertz


def test_should_adjust_frequency():
    old_pitch = Pitch.from_scientific_notation("F#4")
    new_pitch = old_pitch.adjust(5)
    assert old_pitch.frequency == 369.9944227116344
    assert new_pitch.frequency == 493.8833012561241
    assert new_pitch is not old_pitch


def test_should_be_immutable():
    pitch = Pitch.from_scientific_notation("C")
    with pytest.raises(dataclasses.FrozenInstanceError):
        pitch.frequency = 440.0
