import dataclasses
from decimal import Decimal
from fractions import Fraction

import pytest
from digitar.temporal import MeasuredTimeline, Time, Timeline


def test_create_time_from_seconds():
    assert Time(4).seconds == Decimal("4")
    assert Time(4.2).seconds == Decimal("4.2")
    assert Time(Decimal("4.2")).seconds == Decimal("4.2")
    assert Time(Fraction(21, 5)).seconds == Decimal("4.2")
    with pytest.raises(TypeError):
        Time(3 + 2j)


def test_create_time_from_milliseconds():
    assert Time.from_milliseconds(4).seconds == Decimal("0.004")
    assert Time.from_milliseconds(4.2).seconds == Decimal("0.0042")
    assert Time.from_milliseconds(Decimal("4.2")).seconds == Decimal("0.0042")
    assert Time.from_milliseconds(Fraction(21, 5)).seconds == Decimal("0.0042")


def test_time_should_be_immutable():
    time = Time(seconds=0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        time.seconds = Decimal("4.2")


def test_time_add():
    time = Time(seconds=4.2)
    assert (time + Time.from_milliseconds(300)).seconds == Decimal("4.5")
    assert (time + 3).seconds == Decimal("7.2")
    assert (time + 0.3).seconds == Decimal("4.5")
    assert (time + Decimal("0.3")).seconds == Decimal("4.5")
    assert (time + Fraction(3, 10)).seconds == Decimal("4.5")
    with pytest.raises(TypeError):
        time + 3 + 2j


def test_time_mul():
    time = Time(seconds=3.2)
    assert (time * 2).seconds == Decimal("6.4")
    assert (time * 2.5).seconds == Decimal("8.0")
    assert (time * Decimal("2.5")).seconds == Decimal("8.0")
    assert (time * Fraction(1, 4)).seconds == Decimal("0.8")
    with pytest.raises(TypeError):
        time + 3 + 2j


def test_time_num_samples():
    time = Time(seconds=3.2)
    assert time.get_num_samples(44100) == 141120


def test_timeline_create_defaults():
    assert Timeline().instant.seconds == Decimal("0")


def test_timeline_create_at_specific_instant():
    assert Timeline(instant=Time(4.2)).instant.seconds == Decimal("4.2")


def test_timeline_shift_should_return_self():
    timeline = Timeline()
    assert timeline is (timeline >> 4.2)


def test_timeline_shift_should_accept_numeric_types():
    timeline = Timeline()
    timeline >> 1
    timeline >> 0.1
    timeline >> Decimal("0.2")
    timeline >> Fraction(3, 10)
    timeline >> Time(seconds=0.4)
    assert timeline.instant.seconds == 2.0


def test_timeline_shift_exactly():
    timeline = Timeline()
    timeline >> 0.1 >> 0.2
    assert timeline.instant.seconds == Decimal("0.3")


def test_timelines_should_be_independent():
    timeline1 = Timeline() >> 0.1
    timeline2 = Timeline() >> 0.2
    assert timeline1.instant.seconds == Decimal("0.1")
    assert timeline2.instant.seconds == Decimal("0.2")


def test_measured_timeline_create_defaults():
    timeline = MeasuredTimeline()
    assert timeline.instant.seconds == Decimal("0")
    assert timeline.measure.seconds == Decimal("0")
    assert timeline.last_measure_ended_at.seconds == Decimal("0")


def test_measured_timeline_create_at_specific_instant():
    timeline = MeasuredTimeline(instant=Time(4.2))
    assert timeline.instant.seconds == Decimal("4.2")
    assert timeline.measure.seconds == Decimal("0")
    assert timeline.last_measure_ended_at.seconds == Decimal("0")


def test_measured_timeline_create_with_measure():
    timeline = MeasuredTimeline(measure=Time(3.2))
    assert timeline.instant.seconds == Decimal("0")
    assert timeline.measure.seconds == Decimal("3.2")
    assert timeline.last_measure_ended_at.seconds == Decimal("0")


def test_measured_timeline_create_with_measure_at_specific_instant():
    timeline = MeasuredTimeline(instant=Time(6.5), measure=Time(3.2))
    assert timeline.instant.seconds == Decimal("6.5")
    assert timeline.measure.seconds == Decimal("3.2")
    assert timeline.last_measure_ended_at.seconds == Decimal("6.4")


def test_measured_timeline_shift_should_return_self():
    timeline = MeasuredTimeline()
    assert timeline is (timeline >> 4.2)


def test_measured_timeline_shift_should_accept_numeric_types():
    timeline = MeasuredTimeline()
    timeline >> 1
    timeline >> 0.1
    timeline >> Decimal("0.2")
    timeline >> Fraction(3, 10)
    timeline >> Time(seconds=0.4)
    assert timeline.instant.seconds == 2.0


def test_measured_timeline_shift_exactly():
    timeline = MeasuredTimeline()
    timeline >> 0.1 >> 0.2
    assert timeline.instant.seconds == Decimal("0.3")


def test_measured_timelines_should_be_independent():
    timeline1 = MeasuredTimeline() >> 0.1
    timeline2 = MeasuredTimeline() >> 0.2
    assert timeline1.instant.seconds == Decimal("0.1")
    assert timeline2.instant.seconds == Decimal("0.2")


def test_measured_timeline_should_reject_non_positive():
    with pytest.raises(ValueError):
        next(MeasuredTimeline())


def test_measured_timeline_should_reject_non_positive_when_changed():
    timeline = MeasuredTimeline(instant=Time(6.5), measure=Time(3.2))
    timeline.measure = Time(0)
    with pytest.raises(ValueError):
        next(timeline)


def test_measured_timeline_should_jump_to_next_measure():
    timeline = MeasuredTimeline(measure=Time(seconds=3.2))
    assert timeline.instant.seconds == 0
    assert next(timeline).instant.seconds == Decimal("3.2")
    assert next(timeline >> 2.9).instant.seconds == Decimal("6.4")


def test_measured_timeline_should_change_measure():
    timeline = MeasuredTimeline(instant=Time(6.5), measure=Time(3.2))
    assert next(timeline >> 0.4).instant.seconds == Decimal("9.6")
    timeline.measure = Time(seconds=2.0)
    assert next(timeline >> 0.5).instant.seconds == Decimal("11.6")
    assert next(timeline).instant.seconds == Decimal("13.6")
    timeline.measure = Time(seconds=0.905)
    assert next(timeline >> 0.1).instant.seconds == Decimal("14.505")
