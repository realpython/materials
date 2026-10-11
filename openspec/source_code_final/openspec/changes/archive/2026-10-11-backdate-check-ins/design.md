# Design

## Context

See proposal.md for motivation and specs/habit-check-in/spec.md for the required behavior.

Relevant current state:
- `Tracker.check_in(name, day=None, today=None)` in `habits/tracker.py` enforces three rules: no future dates, no more than `MAX_BACKDATE_DAYS = 1` days in the past, and no duplicate day. It raises `ValueError` for each. `today` is injectable, which the tracker tests use.
- `habits/cli.py` computes the day for `done` as `date.today()` minus 1 if `--yesterday` is set, calls `check_in()` without `today`, and turns `KeyError`/`ValueError` into `Error: ...` on stderr with exit status 1. Saving happens only after a successful command, so a rejected check-in never touches the data file.
- `tests/test_tracker.py::test_cannot_backdate_more_than_one_day` asserts the rule being changed.
- Storage keeps check-ins as sorted ISO date strings, so arbitrary past dates need no format change.

## Goals / Non-Goals

**Goals:**
- Keep check-in rules in `Tracker`, testable with injected dates.
- Keep `--yesterday` working exactly as before.

**Non-Goals:**
- Undoing or deleting check-ins, date ranges, or relative dates like `3d` or `last-tuesday`.
- Tracking a habit's creation date to bound backfills.

## Decisions

**1. Raise the backdate limit to 7 days rather than delete it.**
Set `MAX_BACKDATE_DAYS = 7` and change its error to "you can only check in up to 7 days back" (built from the constant). The check stays `(today - day).days > MAX_BACKDATE_DAYS`, so 7 days ago is allowed and 8 is rejected. The future-date and duplicate checks stay as they are, so the method signature and its other callers are unchanged. Add a short comment on the constant pointing to the spec's reason, so it isn't mistaken for an arbitrary number.
- Alternative: remove the limit entirely. Rejected: the limit exists so streaks stay honest, and unlimited backfills would let users rebuild long streaks after the fact (see the "Backfills are limited to 7 days" requirement).

**2. Parse `--date` with an argparse `type=` function based on `date.fromisoformat`.**
A bad value raises `argparse.ArgumentTypeError`, so argparse prints usage plus "invalid date ... expected YYYY-MM-DD" and exits with status 2 before the data file is loaded. This matches how argparse already reports other usage errors.
- Alternative: accept the raw string and validate in `main()`, reporting exit status 1 like tracker errors. This was rejected because a malformed argument is a usage error, and argparse already does the work.
- Python 3.11+ `fromisoformat` also accepts forms like `20261008`. That's harmless, and the documented form stays `YYYY-MM-DD`.

**3. Make `--yesterday` and `--date` a mutually exclusive argparse group.**
argparse rejects the combination with exit status 2, and no extra code is needed.

**4. Resolve "today" once in the CLI and pass it to `check_in()`.**
`main()` computes `today = date.today()`, derives `day` from `--date`, `--yesterday`, or today, and calls `check_in(name, day, today=today)`. That way the future check and the "is this today?" test for the confirmation message use the same date, even across midnight.

**5. Confirmation names the date only for past days.**
For today it stays `Checked in 'read'. Streak: N`. Otherwise it's `Checked in 'read' for 2026-10-08. Streak: N`. The existing output stays stable, and a mistyped backfill date is visible right away.

## Risks / Trade-offs

- [A typo in `--date` records the wrong day, and there's no undo command] → Typos that land more than 7 days back (such as `2025` instead of `2026`) are rejected by the limit. Within the window, the confirmation echoes the date. Removing check-ins is a possible follow-up. For now the JSON file can be edited by hand.
- [Backfilling lets users record days they didn't actually do the habit] → Bounded by the 7-day window, which keeps streaks honest while covering a missed weekend or short trip.
- [A user away for more than 7 days can't backfill the whole gap] → Accepted on purpose; that streak resets.
- [CLI tests depend on the real `date.today()`] → CLI tests build dates relative to `date.today()`. Exact date edge cases are covered in tracker tests with an injected `today`.

## Open Questions

None. Backfill bound resolved: 7 days (see Decision 1).
