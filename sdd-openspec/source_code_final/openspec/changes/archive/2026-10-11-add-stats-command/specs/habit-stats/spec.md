# Spec Delta

## Purpose

Lets users see how they are doing with each tracked habit by reporting its current streak, longest streak, and total check-ins from the command line.

## ADDED Requirements

### Requirement: Stats command lists every habit
The `habits stats` command SHALL print a header row followed by exactly one row per tracked habit, in the same order as `habits list`. Each row SHALL show the habit name, its current streak, its longest streak, and its total check-ins. The command SHALL take no positional arguments and SHALL exit with status 0.

#### Scenario: Several habits are tracked
- **WHEN** the user tracks the habits `read` and `walk` and runs `habits stats`
- **THEN** the output contains a header row naming the columns habit, current streak, longest streak, and total check-ins
- **AND** the output contains one row for `read` and one row for `walk`, in the order they appear in `habits list`
- **AND** the command exits with status 0

#### Scenario: Habit with no check-ins
- **WHEN** the user has added the habit `read` but never checked it in, and runs `habits stats`
- **THEN** the row for `read` shows a current streak of 0, a longest streak of 0, and 0 total check-ins

### Requirement: Current streak matches existing streak rules
The current streak reported by `habits stats` SHALL equal the streak shown by `habits list` for the same habit on the same day: the number of consecutive checked-in days ending today, or ending yesterday when today has no check-in yet.

#### Scenario: Checked in today and yesterday
- **WHEN** `read` has check-ins for today and yesterday only
- **THEN** `habits stats` reports a current streak of 2 for `read`

#### Scenario: Not yet checked in today
- **WHEN** `read` has check-ins for yesterday and the day before, but not today
- **THEN** `habits stats` reports a current streak of 2 for `read`

#### Scenario: Streak is broken
- **WHEN** the most recent check-in for `read` is three days ago
- **THEN** `habits stats` reports a current streak of 0 for `read`

### Requirement: Longest streak covers the full history
The longest streak SHALL be the length of the longest run of consecutive calendar days with a check-in anywhere in the habit's history, including the current streak. It SHALL never be less than the current streak.

#### Scenario: Past run is longer than the current one
- **WHEN** `read` was checked in on five consecutive days last month, missed a day, and has a current streak of 2
- **THEN** `habits stats` reports a longest streak of 5 for `read`

#### Scenario: Current run is the longest
- **WHEN** `read` has a current streak of 4 and no earlier run longer than 4 days
- **THEN** `habits stats` reports a longest streak of 4 for `read`

#### Scenario: Only isolated check-ins
- **WHEN** `read` has three check-ins, none on consecutive days
- **THEN** `habits stats` reports a longest streak of 1 for `read`

### Requirement: Total check-ins counts distinct days
The total check-ins SHALL be the number of distinct days on which the habit was checked in, across its whole history.

#### Scenario: Check-ins with gaps
- **WHEN** `read` has check-ins on 7 different days, with gaps between some of them
- **THEN** `habits stats` reports 7 total check-ins for `read`

### Requirement: Empty tracker shows a hint
When no habits are tracked, `habits stats` SHALL print a single line telling the user to add a habit with `habits add`, SHALL print no table, and SHALL exit with status 0.

#### Scenario: No habits tracked
- **WHEN** the data file is missing or contains no habits, and the user runs `habits stats`
- **THEN** the output is a hint that mentions `habits add`
- **AND** no header row is printed
- **AND** the command exits with status 0

### Requirement: Stats command is read-only
Running `habits stats` SHALL NOT add, remove, or change any habit or check-in, and SHALL NOT create the data file when it does not exist.

#### Scenario: Existing data is untouched
- **WHEN** the user runs `habits stats` with an existing data file
- **THEN** the habits and check-ins stored in the data file are unchanged afterward

#### Scenario: Missing data file is not created
- **WHEN** the data file does not exist and the user runs `habits stats`
- **THEN** the data file still does not exist afterward
