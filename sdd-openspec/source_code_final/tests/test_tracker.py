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


def test_can_backdate_four_days(tracker):
    day = TODAY - timedelta(days=4)
    tracker.check_in("read", day, today=TODAY)
    assert tracker.habits["read"].check_ins == {day}


def test_can_backdate_exactly_seven_days(tracker):
    day = TODAY - timedelta(days=7)
    tracker.check_in("read", day, today=TODAY)
    assert tracker.habits["read"].check_ins == {day}


def test_cannot_backdate_more_than_seven_days(tracker):
    with pytest.raises(ValueError, match="up to 7 days back"):
        tracker.check_in("read", TODAY - timedelta(days=8), today=TODAY)
    assert tracker.habits["read"].check_ins == set()


def test_one_check_in_per_past_day(tracker):
    day = TODAY - timedelta(days=4)
    tracker.check_in("read", day, today=TODAY)
    with pytest.raises(ValueError, match=f"already checked in for {day}"):
        tracker.check_in("read", day, today=TODAY)
    assert tracker.habits["read"].check_ins == {day}


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


def test_total_check_ins_is_zero_without_check_ins(tracker):
    assert tracker.total_check_ins("read") == 0


def test_total_check_ins_counts_distinct_days_with_gaps(tracker):
    tracker.habits["read"].check_ins = {
        TODAY - timedelta(days=offset) for offset in (0, 1, 3, 4, 8, 15, 30)
    }
    assert tracker.total_check_ins("read") == 7


def test_total_check_ins_unknown_habit_raises(tracker):
    with pytest.raises(KeyError):
        tracker.total_check_ins("walk")


def test_longest_streak_is_zero_without_check_ins(tracker):
    assert tracker.longest_streak("read") == 0


def test_longest_streak_of_isolated_days_is_one(tracker):
    tracker.habits["read"].check_ins = {
        TODAY - timedelta(days=offset) for offset in (0, 2, 5)
    }
    assert tracker.longest_streak("read") == 1


def test_longest_streak_finds_past_run_longer_than_current(tracker):
    past_run = {TODAY - timedelta(days=offset) for offset in range(30, 35)}
    current_run = {TODAY, TODAY - timedelta(days=1)}
    tracker.habits["read"].check_ins = past_run | current_run
    assert tracker.streak("read", today=TODAY) == 2
    assert tracker.longest_streak("read") == 5


def test_longest_streak_can_be_current_run(tracker):
    past_run = {TODAY - timedelta(days=offset) for offset in range(10, 13)}
    current_run = {TODAY - timedelta(days=offset) for offset in range(4)}
    tracker.habits["read"].check_ins = past_run | current_run
    assert tracker.streak("read", today=TODAY) == 4
    assert tracker.longest_streak("read") == 4


def test_longest_streak_unknown_habit_raises(tracker):
    with pytest.raises(KeyError):
        tracker.longest_streak("walk")


def test_backfilling_a_gap_restores_current_streak(tracker):
    for offset in (0, 3, 4):
        tracker.check_in("read", TODAY - timedelta(days=offset), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 1
    for offset in (1, 2):
        tracker.check_in("read", TODAY - timedelta(days=offset), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 5


def test_backfill_that_leaves_a_gap_keeps_current_streak(tracker):
    tracker.check_in("read", TODAY, today=TODAY)
    tracker.check_in("read", TODAY - timedelta(days=3), today=TODAY)
    assert tracker.streak("read", today=TODAY) == 1
    assert tracker.total_check_ins("read") == 2
