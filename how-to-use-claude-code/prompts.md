# Prompts

These are the prompts used in the Real Python tutorial
[How to Use Claude Code to Write and Debug Python](https://realpython.com/how-to-use-claude-code/),
in the order they appear.

Claude Code is nondeterministic, so your results will differ in wording and
detail. Expect the same general shape, not identical output.

## 1. Plan the project structure (Plan Mode)

```text
I want to build a minimal command-line contact manager in Python.

It should have two commands:

- `add` to append a new contact with name, email, and phone to a CSV file
- `list` to print all contacts in a readable table format

Use `argparse` for the CLI. Store the CSV at ~/.mini-contacts.csv
by default with a --path flag to override it.

Split the project into a mini_contacts/ package with storage.py for CSV
read/write and cli.py for the `argparse` interface.
```

## 2. Implement the plan

```text
Implement the plan.
```

## 3. Exercise the happy path

```text
Add a contact named "John Doe" with email john@example.com and
phone 555-0100, then list all contacts to verify it was saved.
```

## 4. Write the tests

```text
Write tests for the storage and CLI modules. Cover the happy path for
add and list, and test what happens when the CSV file doesn't exist yet.
```

## 5. Run the tests with Shell mode

```text
! python -m unittest
```

## 6. Commit the initial implementation

```text
Create a commit with the message "Add initial mini-contacts implementation".
```

## 7. Explore the codebase in a fresh session

```text
Review this codebase. Tell me what the application does, describe
each module and how they connect, and summarize the test coverage.
```

## 8. Hunt for bugs and edge cases

```text
Now look for bugs, security issues, and edge cases that could cause
crashes or data loss. Be specific about each finding.
```

## 9. Plan the fixes (Plan Mode)

```text
Fix the crash bug and the edge case for empty-string validation.
For the crash on short CSV rows, handle rows with missing fields gracefully.
For the empty-string fields, reject blank values for name, email, and phone.
```

## 10. Implement the fixes

```text
Implement the fixes.
```

## 11. Re-run the tests

```text
Run the tests and show me the results.
```

## 12. Commit the fixes

```text
Create a commit with the message "Add input validation and fix the crash bug".
```
