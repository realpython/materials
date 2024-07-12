from pathlib import Path
from unittest.mock import mock_open, patch

import pytest
from pydantic_core import Url
from tablature.models import Measure, Note, Song

TEST_TAB = """\
---
title: Hello, World!
artist: John Doe
tracks:
  acoustic:
    url: https://www.songsterr.com/hello
    weight: 0.8
    instrument:
      tuning: [E2, A2, D3, G3, B3, E4]
      vibration: 5.5
      damping: 0.498
      effects:
      - Reverb
      - Convolution:
          impulse_response_filename: acoustic.wav
          mix: 0.95
    tablature:
      beats_per_minute: 75
      measures:
      - time_signature: 4/4
        notes:
        - frets: [0, 0, 2, 2, 0, ~]
          offset: 1/8
          upstroke: true
          arpeggio: 0.04
          vibration: 3.5
      - time_signature: 4/4
      - time_signature: 4/4
        notes: &loop
        - frets: &seven [~, ~, ~, ~, 7, ~]
        - frets: *seven
          offset: 1/4
        - frets: *seven
          offset: 1/4
        - frets: *seven
          offset: 1/4
      - time_signature: 4/4
        notes: *loop
"""


@pytest.fixture
@patch.object(Path, "open", mock_open(read_data=TEST_TAB))
def track():
    song = Song.from_file(Path("/path/to/tab.yaml"))
    return song.tracks["acoustic"]


@pytest.fixture
def instrument(track):
    return track.instrument


@pytest.fixture
def tablature(track):
    return track.tablature


@pytest.fixture
def measures(track):
    return track.tablature.measures


@patch.object(Path, "open", mock_open(read_data=TEST_TAB))
def test_load_song_from_file():
    song = Song.from_file(Path("/path/to/tab.yaml"))
    assert song.title == "Hello, World!"
    assert song.artist == "John Doe"
    assert len(song.tracks) == 1


def test_track(track):
    assert track.url == Url("https://www.songsterr.com/hello")
    assert track.weight == 0.8


def test_instrument(instrument):
    assert instrument.tuning == ["E2", "A2", "D3", "G3", "B3", "E4"]
    assert instrument.vibration == 5.5
    assert instrument.damping == 0.498
    assert instrument.effects == (
        "Reverb",
        {
            "Convolution": {
                "impulse_response_filename": "acoustic.wav",
                "mix": 0.95,
            }
        },
    )


def test_tablature(tablature):
    assert tablature.beats_per_minute == 75
    assert len(tablature.measures) == 4


def test_measures(measures):
    assert measures == (
        Measure(
            time_signature="4/4",
            notes=(
                Note(
                    frets=[0, 0, 2, 2, 0, None],
                    offset="1/8",
                    upstroke=True,
                    arpeggio=0.04,
                    vibration=3.5,
                ),
            ),
        ),
        Measure(time_signature="4/4", notes=()),
        Measure(
            time_signature="4/4",
            notes=(
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="0/1",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
            ),
        ),
        Measure(
            time_signature="4/4",
            notes=(
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="0/1",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
                Note(
                    frets=[None, None, None, None, 7, None],
                    offset="1/4",
                    upstroke=False,
                    arpeggio=0.005,
                    vibration=None,
                ),
            ),
        ),
    )
