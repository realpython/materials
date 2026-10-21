# Design

## Context

See proposal.md for motivation and specs/habit-stats/spec.md for the required behavior.

Relevant current state:
- `Tracker` in `habits/tracker.py` holds `Habit` objects keyed by normalized name, in insertion order (which is also file order after `storage.load`). Each `Habit` stores `check_ins` as a `set[date]`.
- `Tracker.streak(name, today=None)` already computes the current streak, including the "still alive until end of today" rule. It accepts an injectable `today`, which the tests use for deterministic dates.
- `habits/cli.py:main()` loads the tracker, dispatches on the subcommand, then unconditionally calls `storage.save()` before returning 0. That means `list` currently rewrites the file, and creates it if missing.
- There are no CLI tests today; tests cover `Tracker` and `storage` directly.

## Goals / Non-Goals

**Goals:**
- Keep the statistics logic in `Tracker` so it is unit-testable with fixed dates, as the existing streak tests are.
- Keep the CLI layer thin: it formats numbers the tracker computes.

**Non-Goals:**
- Changing how `list`, `add`, or `done` save data, beyond what `stats` itself needs.
- Caching or persisting computed statistics.

## Decisions

**1. Add `Tracker.longest_streak(name)` and `Tracker.total_check_ins(name)`; reuse `Tracker.streak()` for the current streak.**
Both new methods look up the habit through `_get()`, so name normalization and the "no habit named ..." error behave the same as `streak()`. Reusing `streak()` keeps `stats` and `list` consistent by construction.
- Alternative: one `Tracker.stats(name)` returning a dataclass or tuple. It's neater for the CLI, but it adds a type for three integers and makes each figure harder to test on its own. It's easy to add later if more figures appear.

**2. Compute the longest streak by sorting the check-in dates once and scanning for consecutive runs.**
Walk the sorted dates. When a date is exactly one day after the previous one, extend the current run. Otherwise, start a new run of 1. Track the maximum and return 0 for no check-ins. This is O(n log n) in the number of check-ins and needs no `today`, since history isn't affected by the current date.
- Alternative: for each date whose previous day is absent, count forward through the set. That's O(n) but slightly harder to read. Personal habit data is small, so readability wins.

**3. `total_check_ins` is `len(habit.check_ins)`.**
The set already guarantees distinct days, and `check_in()` rejects duplicates.

**4. `stats` returns before the save step.**
In `cli.main()`, the `stats` branch prints its output and returns 0 without reaching `storage.save()`. That satisfies the read-only requirement, including not creating a missing data file. The existing save path for other commands stays untouched.
- Alternative: make `save` conditional for all read-only commands, `list` included. That's cleaner overall, but it changes `list`'s side effects, which is outside this change's scope. It's noted as a possible follow-up.

**5. Output format.**
Print a header row and one row per habit, column-aligned with f-string widths in the style of `list` (name left-aligned in 20 characters, numbers right-aligned). Suggested header: `Habit  Current  Longest  Total`. The exact widths and labels are an implementation detail, as long as the spec's columns and order hold. When `tracker.habits` is empty, print `No habits yet. Add one with 'habits add <name>'.` instead.

## Risks / Trade-offs

- [Long habit names (over 20 characters) push numbers out of alignment, as they already do in `list`] → Accept for consistency with `list`. It's cosmetic, and the values still parse unambiguously.
- [`stats` and `list` now differ in whether they rewrite the data file] → Documented as an intentional scope limit. A follow-up can align `list`.
- [Calling `main()` in tests reads `HABITS_FILE`] → CLI tests set `HABITS_FILE` to a `tmp_path` file via `monkeypatch`, so the user's real `~/.habits.json` is never touched.
- [Current-streak CLI output depends on the real `date.today()`] → CLI tests build check-ins relative to `date.today()`. Exact streak edge cases are covered in `Tracker` unit tests with injected dates.
