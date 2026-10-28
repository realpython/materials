# Tasks

## 1. Tracker statistics

- [x] 1.1 Add `Tracker.total_check_ins(name)` in `habits/tracker.py`, which returns the number of distinct check-in days via `_get()`. Add tests in `tests/test_tracker.py` for 0 check-ins, several check-ins with gaps, and an unknown habit raising `KeyError`. Verify with `uv run pytest tests/test_tracker.py`.
- [x] 1.2 Add `Tracker.longest_streak(name)` in `habits/tracker.py`, which sorts the dates and scans for consecutive runs as in design decision 2. Add tests in `tests/test_tracker.py` for: no check-ins (0), only isolated days (1), a past run longer than the current one (5 vs 2), the current run being the longest, and an unknown habit raising `KeyError`. Verify with `uv run pytest tests/test_tracker.py`.

## 2. `stats` command

- [x] 2.1 Register a `stats` subparser in `habits/cli.py` with the help text "show streaks and totals for each habit" and no arguments. Verify that `uv run habits --help` lists `stats`.
- [x] 2.2 Implement the `stats` branch in `cli.main()`. Print a header row and one aligned row per habit (name, `tracker.streak()`, `longest_streak()`, `total_check_ins()`) in `tracker.habits` order. Print the `habits add` hint when there are no habits, and return 0 before `storage.save()`. Verify with the CLI tests in 2.3.
- [x] 2.3 Add `tests/test_cli.py`. Use `monkeypatch` to point `HABITS_FILE` at a `tmp_path` file and `capsys` to capture output. Cover: the header plus one row per habit in `list` order, with correct current, longest, and total figures (dates relative to `date.today()`); a habit with no check-ins showing 0/0/0; the empty-tracker hint with exit status 0; the data file contents unchanged after `stats`; and a missing data file not being created. Verify with `uv run pytest tests/test_cli.py`.
- [x] 2.4 Add `$ habits stats` to the usage example in `README.md`. Verify that the README example matches the implemented command name.

## 3. Integration check

- [x] 3.1 Run the full test suite with `uv run pytest`, and confirm everything passes, including the existing streak tests.
- [x] 3.2 Run a manual smoke test against a temp data file: `HABITS_FILE=/tmp/h.json uv run habits stats` (prints the hint and creates no file), then `add read`, `done read`, `done read --yesterday`, and `stats` (shows `read` with current 2, longest 2, total 2). Confirm that `openspec validate add-stats-command` passes.
