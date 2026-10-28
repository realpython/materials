# habit-check-in Specification

## Purpose
Lets users record that they did a tracked habit on a given day with `habits done`, including filling in days they forgot to log, under rules that keep the check-in history trustworthy.

## Requirements

### Requirement: Check-in defaults to today
Running `habits done <name>` with no date option SHALL record a check-in for today, SHALL print a confirmation that includes the habit's current streak, and SHALL exit with status 0.

#### Scenario: Check in today
- **WHEN** the user tracks `read` and runs `habits done read`
- **THEN** a check-in for today is stored for `read`
- **AND** the output confirms the check-in and shows the current streak
- **AND** the command exits with status 0

#### Scenario: Unknown habit
- **WHEN** no habit named `walk` is tracked and the user runs `habits done walk`
- **THEN** the command prints an error naming `walk` and exits with a non-zero status
- **AND** no check-in is stored

### Requirement: Check-in for a recent past day
`habits done <name> --date YYYY-MM-DD` SHALL record the check-in for that calendar day, for any date from 7 days before today up to and including today. When the date is not today, the confirmation SHALL name the date.

#### Scenario: Backfill a day several days ago
- **WHEN** today is 2026-10-12 and the user runs `habits done read --date 2026-10-08`
- **THEN** a check-in for 2026-10-08 is stored for `read`
- **AND** the confirmation mentions 2026-10-08
- **AND** the command exits with status 0

#### Scenario: Date equal to today
- **WHEN** today is 2026-10-12 and the user runs `habits done read --date 2026-10-12`
- **THEN** a check-in for today is stored, the same as `habits done read`

### Requirement: Backfills are limited to 7 days
A check-in for a date more than 7 days before today SHALL be rejected with an error stating the 7-day limit, a non-zero exit status, and no change to stored check-ins. The limit is deliberate, so streaks stay honest: users can catch up on recently forgotten days but cannot rebuild long streaks after the fact. It SHALL NOT be removed; it widens the earlier today-or-yesterday limit.

#### Scenario: Oldest allowed day
- **WHEN** today is 2026-10-12 and the user runs `habits done read --date 2026-10-05`
- **THEN** a check-in for 2026-10-05 is stored for `read`
- **AND** the command exits with status 0

#### Scenario: Older than the limit
- **WHEN** today is 2026-10-12 and the user runs `habits done read --date 2026-10-04`
- **THEN** the command prints an error saying check-ins can be at most 7 days back and exits with a non-zero status
- **AND** no check-in is stored

### Requirement: Yesterday shortcut is kept
`habits done <name> --yesterday` SHALL record the check-in for the day before today. `--yesterday` and `--date` SHALL NOT be accepted together; combining them SHALL be rejected with a non-zero exit status and no check-in stored.

#### Scenario: Check in yesterday
- **WHEN** today is 2026-10-12 and the user runs `habits done read --yesterday`
- **THEN** a check-in for 2026-10-11 is stored for `read`

#### Scenario: Both options given
- **WHEN** the user runs `habits done read --yesterday --date 2026-10-08`
- **THEN** the command exits with a non-zero status
- **AND** no check-in is stored

### Requirement: Future and invalid dates are rejected
A check-in for a date after today SHALL be rejected. A `--date` value that is not a valid calendar date in `YYYY-MM-DD` form SHALL be rejected. In both cases the command SHALL print an error, exit with a non-zero status, and leave stored check-ins unchanged.

#### Scenario: Future date
- **WHEN** today is 2026-10-12 and the user runs `habits done read --date 2026-10-13`
- **THEN** the command prints an error saying future dates aren't allowed and exits with a non-zero status
- **AND** no check-in is stored

#### Scenario: Malformed date
- **WHEN** the user runs `habits done read --date 2026-02-30` or `habits done read --date last-tuesday`
- **THEN** the command prints an error about the date format and exits with a non-zero status
- **AND** no check-in is stored

### Requirement: One check-in per habit per day
A habit SHALL have at most one check-in per calendar day. Checking in a habit for a day that already has a check-in, whether today or a past date, SHALL print an error naming the day, exit with a non-zero status, and leave stored check-ins unchanged.

#### Scenario: Duplicate backfill
- **WHEN** `read` already has a check-in for 2026-10-08 and the user runs `habits done read --date 2026-10-08`
- **THEN** the command prints an error saying `read` is already checked in for 2026-10-08 and exits with a non-zero status
- **AND** `read` still has exactly one check-in for 2026-10-08

#### Scenario: Duplicate today
- **WHEN** `read` already has a check-in for today and the user runs `habits done read`
- **THEN** the command exits with a non-zero status and the check-ins are unchanged

### Requirement: Backfilled check-ins count toward streaks
A check-in recorded for a past day SHALL be treated exactly like one recorded on that day: it SHALL count toward the current streak, longest streak, and total check-ins under the existing streak rules.

#### Scenario: Filling a gap restores the current streak
- **WHEN** today is 2026-10-12, `read` has check-ins for 2026-10-12, 2026-10-09, and 2026-10-08, and the user runs `habits done read --date 2026-10-11` and then `habits done read --date 2026-10-10`
- **THEN** the current streak for `read` is 5

#### Scenario: Backfill that leaves a gap
- **WHEN** today is 2026-10-12, `read` has a check-in only for today, and the user runs `habits done read --date 2026-10-09`
- **THEN** the current streak for `read` is 1
- **AND** the total check-ins for `read` is 2
