import os
from argparse import ArgumentParser, Namespace
from contextlib import contextmanager
from fractions import Fraction
from pathlib import Path

import numpy as np
import pedalboard
from digitar.chord import Chord
from digitar.instrument import PluckedStringInstrument, StringTuning
from digitar.processing import normalize
from digitar.stroke import Velocity
from digitar.synthesis import Synthesizer
from digitar.temporal import MeasuredTimeline, Time
from digitar.track import AudioTrack
from pedalboard.io import AudioFile

from tablature import models

SAMPLING_RATE = 44100


def main() -> None:
    play(parse_args())


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("path", type=Path, help="tablature file (.yaml)")
    parser.add_argument("-o", "--output", type=Path, default=None)
    return parser.parse_args()


def play(args: Namespace) -> None:
    song = models.Song.from_file(args.path)
    with chdir(args.path.parent):
        samples = normalize(
            np.sum(
                pad_to_longest(
                    [
                        track.weight * synthesize(track)
                        for track in song.tracks.values()
                    ]
                ),
                axis=0,
            )
        )
    save(
        samples,
        args.output or Path.cwd() / args.path.with_suffix(".mp3").name,
    )


@contextmanager
def chdir(directory: Path) -> None:
    current_dir = os.getcwd()
    os.chdir(directory)
    try:
        yield
    finally:
        os.chdir(current_dir)


def pad_to_longest(tracks: list[np.ndarray]) -> list[np.ndarray]:
    max_length = max(array.size for array in tracks)
    return [np.pad(array, (0, max_length - array.size)) for array in tracks]


def save(samples: np.ndarray, path: Path) -> None:
    with AudioFile(str(path), "w", SAMPLING_RATE) as file:
        file.write(samples)
    print(f"Saved file {path.absolute()}")


def synthesize(track: models.Track) -> np.ndarray:
    synthesizer = Synthesizer(
        instrument=PluckedStringInstrument(
            tuning=StringTuning.from_notes(*track.instrument.tuning),
            damping=track.instrument.damping,
            vibration=Time(track.instrument.vibration),
        ),
        sampling_rate=SAMPLING_RATE,
    )
    audio_track = AudioTrack(synthesizer.sampling_rate)
    timeline = MeasuredTimeline()
    read(track.tablature, synthesizer, audio_track, timeline)
    return apply_effects(audio_track, track.instrument)


def read(
    tablature: models.Tablature,
    synthesizer: Synthesizer,
    audio_track: AudioTrack,
    timeline: MeasuredTimeline,
) -> None:
    beat = Time(seconds=60 / tablature.beats_per_minute)
    for measure in tablature.measures:
        timeline.measure = beat * measure.beats_per_measure
        whole_note = beat * measure.note_value.denominator
        for note in measure.notes:
            stroke = Velocity.up if note.upstroke else Velocity.down
            audio_track.add_at(
                (timeline >> (whole_note * Fraction(note.offset))).instant,
                synthesizer.strum_strings(
                    chord=Chord(note.frets),
                    velocity=stroke(delay=Time(note.arpeggio)),
                    vibration=(
                        Time(note.vibration) if note.vibration else None
                    ),
                ),
            )
        next(timeline)


def apply_effects(
    audio_track: AudioTrack, instrument: models.Instrument
) -> np.ndarray:
    effects = pedalboard.Pedalboard(get_plugins(instrument))
    return effects(audio_track.samples, audio_track.sampling_rate)


def get_plugins(instrument: models.Instrument) -> list[pedalboard.Plugin]:
    return [get_plugin(effect) for effect in instrument.effects]


def get_plugin(effect: str | dict) -> pedalboard.Plugin:
    match effect:
        case str() as class_name:
            return getattr(pedalboard, class_name)()
        case dict() as plugin_dict if len(plugin_dict) == 1:
            class_name, params = list(plugin_dict.items())[0]
            return getattr(pedalboard, class_name)(**params)
