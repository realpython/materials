import pytest
from digitar.chord import Chord


@pytest.fixture
def fret_numbers():
    return [4, None, None, 3, 4, 0]


def test_create_from_sequence(fret_numbers):
    assert Chord(fret_numbers) == tuple(fret_numbers)


def test_create_from_numbers(fret_numbers):
    assert Chord.from_numbers(*fret_numbers) == tuple(fret_numbers)


def test_should_contain_none(fret_numbers):
    assert None in Chord(fret_numbers)


def test_should_be_immutable(fret_numbers):
    chord = Chord(fret_numbers)
    with pytest.raises(TypeError):
        chord[0] = 42
