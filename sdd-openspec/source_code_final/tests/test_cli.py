import json
from datetime import date, timedelta

import pytest

from habits.cli import main


def days_ago(*offsets):
    today = date.today()
    return [(today - timedelta(days=offset)).isoformat() for offset in offsets]


@pytest.fixture
def habits_file(tmp_path, monkeypatch):
    path = tmp_path / "habits.json"
    monkeypatch.setenv("HABITS_FILE", str(path))
    return path


def run_stats(capsys):
    status = main(["stats"])
    return status, capsys.readouterr().out.splitlines()


def test_stats_prints_header_and_one_row_per_habit_in_list_order(
    habits_file, capsys
):
    habits_file.write_text(
        json.dumps(
            {
                # Current 2, past run of 5 days, 7 distinct days in total.
                "walk": days_ago(0, 1, 10, 11, 12, 13, 14),
                # Not checked in today: current 3 (ends yesterday), longest 3.
                "read": days_ago(1, 2, 3, 6),
            }
        ),
        encoding="utf-8",
    )

    status, lines = run_stats(capsys)

    assert status == 0
    assert lines[0].split() == ["Habit", "Current", "Longest", "Total"]
    assert [line.split() for line in lines[1:]] == [
        ["walk", "2", "5", "7"],
        ["read", "3", "3", "4"],
    ]

    main(["list"])
    list_order = [
        line.split()[0] for line in capsys.readouterr().out.splitlines()
    ]
    assert list_order == ["walk", "read"]


def test_habit_without_check_ins_shows_zeros(habits_file, capsys):
    habits_file.write_text(json.dumps({"read": []}), encoding="utf-8")

    status, lines = run_stats(capsys)

    assert status == 0
    assert lines[1].split() == ["read", "0", "0", "0"]


def test_empty_tracker_prints_hint(habits_file, capsys):
    habits_file.write_text(json.dumps({}), encoding="utf-8")

    status, lines = run_stats(capsys)

    assert status == 0
    assert len(lines) == 1
    assert "habits add" in lines[0]
    assert "Habit" not in lines[0]


def test_stats_leaves_data_file_unchanged(habits_file, capsys):
    # Compact, unsorted JSON would be rewritten by storage.save(), so an
    # identical file proves stats didn't save.
    original = json.dumps({"read": days_ago(1, 0), "walk": []})
    habits_file.write_text(original, encoding="utf-8")

    run_stats(capsys)

    assert habits_file.read_text(encoding="utf-8") == original


def test_stats_does_not_create_missing_data_file(habits_file, capsys):
    status, lines = run_stats(capsys)

    assert status == 0
    assert "habits add" in lines[0]
    assert not habits_file.exists()


def stored(habits_file, name="read"):
    return json.loads(habits_file.read_text(encoding="utf-8"))[name]


@pytest.fixture
def tracked(habits_file, capsys):
    main(["add", "read"])
    capsys.readouterr()
    return habits_file


def test_done_date_backfills_a_past_day(tracked, capsys):
    (day,) = days_ago(3)
    status = main(["done", "read", "--date", day])
    assert status == 0
    assert day in capsys.readouterr().out
    assert stored(tracked) == [day]


def test_done_date_today_behaves_like_plain_done(tracked, capsys):
    (today,) = days_ago(0)
    status = main(["done", "read", "--date", today])
    assert status == 0
    assert capsys.readouterr().out == "Checked in 'read'. Streak: 1\n"
    assert stored(tracked) == [today]


def test_done_yesterday_still_stores_yesterday(tracked, capsys):
    status = main(["done", "read", "--yesterday"])
    assert status == 0
    assert stored(tracked) == days_ago(1)


def test_done_future_date_is_rejected(tracked, capsys):
    original = tracked.read_text(encoding="utf-8")
    (tomorrow,) = days_ago(-1)
    assert main(["done", "read", "--date", tomorrow]) == 1
    assert "future" in capsys.readouterr().err
    assert tracked.read_text(encoding="utf-8") == original


def test_done_date_beyond_seven_days_is_rejected(tracked, capsys):
    original = tracked.read_text(encoding="utf-8")
    (day,) = days_ago(8)
    assert main(["done", "read", "--date", day]) == 1
    assert "7 days" in capsys.readouterr().err
    assert tracked.read_text(encoding="utf-8") == original


@pytest.mark.parametrize("value", ["2026-02-30", "last-tuesday"])
def test_done_malformed_date_is_rejected(tracked, capsys, value):
    original = tracked.read_text(encoding="utf-8")
    with pytest.raises(SystemExit) as excinfo:
        main(["done", "read", "--date", value])
    assert excinfo.value.code != 0
    assert "YYYY-MM-DD" in capsys.readouterr().err
    assert tracked.read_text(encoding="utf-8") == original


def test_done_yesterday_and_date_cannot_be_combined(tracked, capsys):
    original = tracked.read_text(encoding="utf-8")
    (day,) = days_ago(3)
    with pytest.raises(SystemExit) as excinfo:
        main(["done", "read", "--yesterday", "--date", day])
    assert excinfo.value.code != 0
    assert tracked.read_text(encoding="utf-8") == original


def test_done_duplicate_past_date_is_rejected(tracked, capsys):
    (day,) = days_ago(3)
    assert main(["done", "read", "--date", day]) == 0
    assert main(["done", "read", "--date", day]) == 1
    assert f"already checked in for {day}" in capsys.readouterr().err
    assert stored(tracked) == [day]


def test_done_unknown_habit_is_rejected(tracked, capsys):
    assert main(["done", "walk"]) == 1
    assert "walk" in capsys.readouterr().err
    assert stored(tracked) == []
