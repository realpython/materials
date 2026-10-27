# Proposal

## Why

Users lose streaks when they forget to log a habit for a few days, because `habits done` only accepts today or yesterday. Letting them check in for any day in the past week lets them fill those gaps.

## What Changes

- Add a `--date YYYY-MM-DD` option to `habits done` that records the check-in for that calendar day.
- **Modifies existing behavior**: raises the backdate limit from one day (`MAX_BACKDATE_DAYS = 1`, error "you can only check in for today or yesterday") to 7 days. Older dates are rejected with an error stating the limit.
- Kept unchanged: future dates are rejected; a habit can be checked in at most once per day; `habits done <name>` still means today; `--yesterday` still works.
- `--date` and `--yesterday` cannot be combined. An invalid date is rejected and nothing is saved.
- When the check-in is not for today, the confirmation names the date.
- Backfilled days count toward streaks under the existing streak rules.

Decided:
- Backfills stay bounded, deliberately: the limit exists so streaks stay honest, so it is widened to 7 days rather than removed.

Out of scope:
- Removing check-ins and multi-day ranges in one command are out of scope.

## Capabilities

### New Capabilities
- `habit-check-in`: Recording check-ins for a habit with `habits done`: which days are allowed, duplicate handling, and how the day is chosen.

### Modified Capabilities
None. `habit-stats` rules are unchanged.

## Impact

- `habits/tracker.py`: raise the backdate limit in `Tracker.check_in()` to 7 days and update its error message.
- `habits/cli.py`: add `--date`, make it mutually exclusive with `--yesterday`, adjust the confirmation.
- `tests/`: replace the "cannot backdate more than one day" test; add tracker and CLI tests.
- `README.md`: document `--date`.
- No new dependencies; JSON storage format unchanged.
