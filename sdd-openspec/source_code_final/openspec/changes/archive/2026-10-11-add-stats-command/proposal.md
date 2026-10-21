# Proposal

## Why

Today `habits list` only shows each habit's current streak, so a user has no way to see their best run or how many times they've checked in overall. A single `stats` command gives that progress summary without having to read `~/.habits.json` by hand.

## What Changes

- Add a new `habits stats` subcommand that prints one row per tracked habit with three figures: current streak, longest streak, and total check-ins.
- Current streak uses the same rule as `habits list` and `habits done` today (a streak stays alive until the end of today if yesterday was checked in).
- Longest streak is the longest run of consecutive check-in days anywhere in the habit's history (it can be the current streak).
- Total check-ins is the number of distinct days the habit was checked in.
- When no habits are tracked, `stats` prints a short hint instead of an empty table.
- `stats` is read-only: it doesn't add, change, or rewrite stored check-ins.
- No changes to `add`, `done`, `list`, or the storage format. Nothing is breaking.

Scope decisions (confirmed at review):
- `stats` takes no arguments and always reports every habit. Filtering to one habit (`habits stats read`) is out of scope.
- Output is a plain-text, column-aligned table with a header row, in the same habit order as `habits list`. Machine-readable output (for example `--json`) is out of scope.

## Capabilities

### New Capabilities
- `habit-stats`: Reporting per-habit progress statistics (current streak, longest streak, total check-ins) through the `habits stats` command.

### Modified Capabilities
<!-- None. No specs exist yet, and existing commands keep their behavior. -->

## Impact

- `habits/tracker.py`: new methods on `Tracker` to compute the longest streak and the total check-ins for a habit. The existing `streak()` method is reused unchanged.
- `habits/cli.py`: register the `stats` subparser and print the table.
- `tests/`: new unit tests for the statistics and a CLI-level test for the `stats` output.
- `README.md`: document `habits stats` in the usage example.
- No new dependencies, and no change to the JSON data file.
