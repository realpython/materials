from datetime import date, timedelta

import pytest

from habits.tracker import Tracker

TODAY = date(2026, 10, 12)


@pytest.fixture
def tracker():
    tracker = Tracker()
    tracker.add("Read")
    return tracker


def test_names_are_normalized(tracker):
    assert "read" in tracker.habits


def test_duplicate_habit_is_rejected(tracker):
    with pytest.raises(ValueError):
        tracker.add("read")


def test_one_check_in_per_day(tracker):
    tracker.check_in("read", TODAY, today=TODAY)
    with pytest.raises(ValueError):
        tracker.check_in("read", TODAY, today=TODAY)


def test_cannot_check_in_the_future(tracker):
    with pytest.raises(ValueError):
        tracker.check_in("read", TODAY + timedelta(days=1), today=TODAY)


def test_can_check_in_yesterday(tracker):
    tracker.check_in("read", TODAY - timedelta(days=1), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 1


def test_cannot_backdate_more_than_one_day(tracker):
    with pytest.raises(ValueError):
        tracker.check_in("read", TODAY - timedelta(days=2), today=TODAY)


def test_streak_counts_consecutive_days(tracker):
    for offset in (1, 0):
        tracker.check_in("read", TODAY - timedelta(days=offset), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 2


def test_missed_day_breaks_streak():
    tracker = Tracker()
    habit = tracker.add("read")
    habit.check_ins = {
        TODAY,
        TODAY - timedelta(days=2),
        TODAY - timedelta(days=3),
    }
    assert tracker.streak("read", today=TODAY) == 1


def test_streak_survives_until_end_of_today(tracker):
    tracker.check_in("read", TODAY - timedelta(days=1), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 1
