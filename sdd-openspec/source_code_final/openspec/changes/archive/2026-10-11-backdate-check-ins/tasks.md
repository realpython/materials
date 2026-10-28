# Tasks

## 1. Tracker check-in rules

- [x] 1.1 In `habits/tracker.py`, set `MAX_BACKDATE_DAYS = 7` with a short comment on why it exists (streaks stay honest; see spec), and change the error to "you can only check in up to 7 days back" built from the constant. Keep the future-date and duplicate-day checks (design decision 1). In `tests/test_tracker.py`, replace `test_cannot_backdate_more_than_one_day` with tests (injected `today`) that accept a check-in 4 days ago and exactly 7 days ago, and reject one 8 days ago with the 7-day error and no check-in stored. Keep the existing future-date and duplicate tests, and add a duplicate test for a past date. Verify with `uv run pytest tests/test_tracker.py`.
- [x] 1.2 Add tracker tests for backfilled streaks with an injected `today`: filling a two-day gap brings the current streak to 5, and a backfill that leaves a gap keeps the current streak at 1 with total check-ins at 2. Verify with `uv run pytest tests/test_tracker.py`.

## 2. `done --date` command option

- [x] 2.1 In `habits/cli.py`, put `--yesterday` and a new `--date` option in a mutually exclusive group on the `done` subparser. Parse `--date` with a `date.fromisoformat`-based `type=` function that raises `argparse.ArgumentTypeError` ("expected YYYY-MM-DD") on bad input (design decisions 2 and 3). Verify that `uv run habits done --help` shows both options.
- [x] 2.2 In the `done` branch of `cli.main()`, compute `today = date.today()` once, pick `day` from `--date`, `--yesterday`, or today, and call `check_in(name, day, today=today)`. Print `Checked in '<name>' for <YYYY-MM-DD>. Streak: N` when `day != today`, and keep the existing message otherwise (design decisions 4 and 5). Verify with the CLI tests in 2.3.
- [x] 2.3 Add `done` tests to `tests/test_cli.py` using the existing `habits_file` fixture, with dates relative to `date.today()`. Cover: `--date` 3 days ago stores that day, mentions it in the output, and exits 0; `--date` for today behaves like plain `done`; `--yesterday` still stores yesterday; a future `--date` exits 1 and leaves the file unchanged; a `--date` 8 days ago exits 1, mentions the 7-day limit, and leaves the file unchanged; malformed `--date 2026-02-30` and `--date last-tuesday` raise `SystemExit` with a non-zero code and leave the file unchanged; `--yesterday --date ...` raises `SystemExit` with a non-zero code; a duplicate past date exits 1 and keeps one check-in; and an unknown habit exits 1. Verify with `uv run pytest tests/test_cli.py`.
- [x] 2.4 Add `$ habits done read --date 2026-10-08` to the usage example in `README.md`, with a one-line note that dates up to 7 days back are allowed. Verify that the example runs against a temp `HABITS_FILE`.

## 3. Integration check

- [x] 3.1 Run the full suite with `uv run pytest` and confirm everything passes, including the existing streak and stats tests.
- [x] 3.2 Run a manual smoke test with `HABITS_FILE=/tmp/h.json`: run `add read` and `done read`, then `done read --date` for 3 days ago (streak stays 1), then `--date` for 2 days ago and `--yesterday` (streak becomes 4). Then check that `stats` shows current 4, longest 4, total 4. Confirm that `openspec validate backdate-check-ins --strict` passes.
