from dataclasses import dataclass
from fractions import Fraction

import numpy as np
from digitar.chord import Chord
from digitar.instrument import PluckedStringInstrument, StringTuning
from digitar.processing import normalize
from digitar.stroke import Velocity
from digitar.synthesis import Synthesizer
from digitar.temporal import MeasuredTimeline, Time
from digitar.track import AudioTrack
from pedalboard import Convolution, Gain, LowShelfFilter, Pedalboard, Reverb
from pedalboard.io import AudioFile

BEATS_PER_MINUTE = 75
BEATS_PER_MEASURE = 4
NOTE_VALUE = Fraction(1, 4)


class MeasureTiming:
    BEAT = Time(seconds=60 / BEATS_PER_MINUTE)
    MEASURE = BEAT * BEATS_PER_MEASURE


class Note:
    WHOLE = MeasureTiming.BEAT * NOTE_VALUE.denominator
    SEVEN_SIXTEENTH = WHOLE * Fraction(7, 16)
    FIVE_SIXTEENTH = WHOLE * Fraction(5, 16)
    THREE_SIXTEENTH = WHOLE * Fraction(3, 16)
    ONE_EIGHTH = WHOLE * Fraction(1, 8)
    ONE_SIXTEENTH = WHOLE * Fraction(1, 16)
    ONE_THIRTY_SECOND = WHOLE * Fraction(1, 32)


class StrummingSpeed:
    SLOW = Time.from_milliseconds(40)
    FAST = Time.from_milliseconds(20)
    SUPER_FAST = Time.from_milliseconds(5)


@dataclass(frozen=True)
class Stroke:
    instant: Time
    chord: Chord
    velocity: Velocity


def main() -> None:
    acoustic_guitar = PluckedStringInstrument(
        tuning=StringTuning.from_notes("E2", "A2", "D3", "G3", "B3", "E4"),
        vibration=Time(seconds=10),
        damping=0.498,
    )
    synthesizer = Synthesizer(acoustic_guitar)
    audio_track = AudioTrack(synthesizer.sampling_rate)
    timeline = MeasuredTimeline(measure=MeasureTiming.MEASURE)
    for measure in measures(timeline):
        for stroke in measure:
            audio_track.add_at(
                stroke.instant,
                synthesizer.strum_strings(stroke.chord, stroke.velocity),
            )
    save(audio_track, "diablo.mp3")


def measures(timeline: MeasuredTimeline) -> tuple[tuple[Stroke, ...], ...]:
    return (
        measure_01(timeline),
        measure_02(timeline),
    )


def measure_01(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            timeline.instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 2, None, None, None),
            Velocity.up(StrummingSpeed.FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_02(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.SEVEN_SIXTEENTH).instant,
            Chord.from_numbers(7, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def save(audio_track: AudioTrack, filename: str) -> None:
    with AudioFile(filename, "w", audio_track.sampling_rate) as file:
        file.write(normalize(apply_effects(audio_track)))
    print(f"\nSaved file {filename!r}")


def apply_effects(audio_track: AudioTrack) -> np.ndarray:
    effects = Pedalboard(
        [
            Reverb(),
            Convolution(impulse_response_filename="ir/acoustic.wav", mix=0.95),
            LowShelfFilter(cutoff_frequency_hz=440, gain_db=10, q=1),
            Gain(gain_db=6),
        ]
    )
    return effects(audio_track.samples, audio_track.sampling_rate)


if __name__ == "__main__":
    main()
