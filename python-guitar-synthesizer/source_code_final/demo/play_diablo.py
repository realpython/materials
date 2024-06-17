"""
https://www.songsterr.com/a/wsa/matt-uelmen-diablo-tristram-tab-s502203
"""

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
    for i, measure in enumerate(measures(timeline), 1):
        print("\b" * 15 + f"Progress: {i / 77:.0%}", end="", flush=True)
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
        measure_03(timeline),
        measure_04(timeline),
        measure_05(timeline),
        measure_06(timeline),
        measure_07(timeline),
        measure_08(timeline),
        measure_09(timeline),
        measure_10(timeline),
        measure_11(timeline),
        measure_12(timeline),
        measure_13(timeline),
        measure_14(timeline),
        measure_15(timeline),
        measure_16(timeline),
        measure_17(timeline),
        measure_18(timeline),
        measure_19(timeline),
        measure_20(timeline),
        measure_21(timeline),
        measure_22(timeline),
        measure_23(timeline),
        measure_24(timeline),
        measure_25(timeline),
        measure_26(timeline),
        measure_27(timeline),
        measure_28(timeline),
        measure_29(timeline),
        measure_30(timeline),
        measure_31(timeline),
        measure_32(timeline),
        measure_33(timeline),
        measure_34(timeline),
        measure_35(timeline),
        measure_36(timeline),
        measure_37(timeline),
        measure_38(timeline),
        measure_39(timeline),
        measure_40(timeline),
        measure_41(timeline),
        measure_42(timeline),
        measure_43(timeline),
        measure_44(timeline),
        measure_45(timeline),
        measure_46(timeline),
        measure_47(timeline),
        measure_48(timeline),
        measure_49(timeline),
        measure_50(timeline),
        measure_51(timeline),
        measure_52(timeline),
        measure_53(timeline),
        measure_54(timeline),
        measure_55(timeline),
        measure_56(timeline),
        measure_57(timeline),
        measure_58(timeline),
        measure_59(timeline),
        measure_60(timeline),
        measure_61(timeline),
        measure_62(timeline),
        measure_63(timeline),
        measure_64(timeline),
        measure_65(timeline),
        measure_66(timeline),
        measure_67(timeline),
        measure_68(timeline),
        measure_69(timeline),
        measure_70(timeline),
        measure_71(timeline),
        measure_72(timeline),
        measure_73(timeline),
        measure_74(timeline),
        measure_75(timeline),
        measure_76(timeline),
        measure_77(timeline),
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


def measure_03(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
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


def measure_04(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
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
            Chord.from_numbers(None, 6, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_05(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 3, 2, 0, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 2, None, None, None),
            Velocity.up(StrummingSpeed.FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 3, 2, 0, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.SEVEN_SIXTEENTH).instant,
            Chord.from_numbers(6, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_06(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(6, 5, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(6, 5, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.SEVEN_SIXTEENTH).instant,
            Chord.from_numbers(3, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_07(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 3, 2, 0, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 3, 2, 0, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.SEVEN_SIXTEENTH).instant,
            Chord.from_numbers(6, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_08(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(6, 5, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(6, 5, 7, 8, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.SEVEN_SIXTEENTH).instant,
            Chord.from_numbers(None, 6, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_09(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_10(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_11(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 0, 2, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_12(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 4, 2, 1, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_13(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_14(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_15(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_16(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 1, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_17(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_18(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_19(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_20(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_21(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_22(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_23(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_24(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 3),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_25(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 3, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_26(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 1, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 4, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 5, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(5, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 7, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 8, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(8, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 10, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 10, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 11, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_27(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(12, 12, 12, None, None, None),
            Velocity.down(StrummingSpeed.FAST),
        ),
    )


def measure_28(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(3, 1, 0, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(3, 1, 0, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_29(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, 3, 0, 4, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(2, 3, 0, 4, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_30(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(3, 1, 0, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(3, 1, 0, 2, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_31(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, 3, 0, 4, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(2, 3, 0, 4, 0, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_32(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 1, 2, 3, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(None, None, None, 5, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 7, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 5, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 7, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 5, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 6, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 8, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(5, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_33(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 0, 0, 2, 3, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 0, 0, 2, 3, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_34(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 1, 2, 3, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.THREE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(0, 1, 2, 3, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.FIVE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
    )


def measure_35(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            (next(timeline) >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(None, None, None, 9, None, None),
            Velocity.down(StrummingSpeed.SLOW),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 10, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 9, 7, 7),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_EIGHTH).instant,
            Chord.from_numbers(None, None, None, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 10, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, None, 9, 7, 7),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_36(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_37(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_38(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_39(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 1, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 1, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 1, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 1, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_40(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_41(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_42(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 7, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 6, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 6, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 6, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 6, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 8, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_43(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 11, None, 9, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 10, None, 8, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 7, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 6, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_44(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_45(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_46(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_47(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 3),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_48(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 3, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_49(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 1, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 4, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 5, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(5, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 7, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 7, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 8, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(8, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 10, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 10, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 11, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_50(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_51(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, None, None, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, 0, 9, 9, None, None),
            Velocity.up(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_52(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(8, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_53(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_54(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(6, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(6, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(3, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_55(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_56(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(12, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(11, 12, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(8, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_57(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(7, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 0, 9, 9, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_58(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(7, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(6, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(6, 7, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(3, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_59(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 4, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(2, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(2, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_60(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_61(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 3, 3, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_62(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(None, 2, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_THIRTY_SECOND).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_63(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_64(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_65(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_66(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_67(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 0, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_68(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 3, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_69(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 0, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 2),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 0, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_70(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, 0, None, None, 3),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 5, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_71(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, 2, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_72(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, 1, None, None, 3, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 3, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_73(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, 2, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 3),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_74(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, 3, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(0, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 1, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_75(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, 3, None, 1, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, 1),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 1, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 1, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(1, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_76(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 0, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, None, 0),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 2, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 2, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 2, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 4, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, None, 1, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 3, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 3, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 3, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
    )


def measure_77(timeline: MeasuredTimeline) -> tuple[Stroke, ...]:
    return (
        Stroke(
            next(timeline).instant,
            Chord.from_numbers(None, None, None, None, 2, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, None, 4, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(3, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(3, None, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, None, 0, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(None, 0, None, None, None, None),
            Velocity.down(StrummingSpeed.SUPER_FAST),
        ),
        Stroke(
            (timeline >> Note.ONE_SIXTEENTH).instant,
            Chord.from_numbers(3, 0, 0, 4, 2, None),
            Velocity.down(StrummingSpeed.FAST),
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
