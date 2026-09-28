## Testing Conventions

Write tests with `pytest`. Put them in `tests/test_<module>.py`, mirroring
the package layout.

### Structure

- Arrange, act, assert, in that order, separated by blank lines.
- One behavior per test. If the name needs an "and", split the test.
- Name tests `test_<unit>_<condition>_<expected>`.
- Use `@pytest.mark.parametrize` for table-driven cases, not loops.

### Assertions

- Assert exact values, never types: `assert total == Decimal("190.00")`,
  not `assert isinstance(total, Decimal)`.
- Take expected values from `BEHAVIOR.md`. Never call the code under
  test to produce an expected value, and never reimplement its
  arithmetic in the test.
- Match the full exception message, anchored with `^` and `$`:
  `pytest.raises(ValueError, match="^unknown tier: gold$")`.
  Never `pytest.raises(Exception)`.
- Assert on returned values and raised errors, not on
  `assert_called_once_with`.

### Coverage

- Parametrize both sides of every boundary in `BEHAVIOR.md`. For a
  threshold at 10, test 9, 10, and 11.
- One test per error path.
- Cover empty, missing, and zero inputs.

### Mocking

- Mock only what you can't control or can't afford: clocks, randomness,
  network calls, subprocesses, slow or destructive operations.
- Never mock the module under test.
- Never mock code we own just to avoid setting it up. Use a
  fixture instead.
- For files, use `tmp_path` and real files rather than patching `open`.

### Quality Gates

Before reporting a suite as done, run these yourself and keep working until
they pass:

- `pytest` passes.
- `pytest --cov=<module> --cov-branch --cov-report=term-missing` reports at
  least 95% branch coverage on the module under test.

Then report the coverage number.

## Behavior Tables

Record intended behavior in `BEHAVIOR.md`, one section per public
callable, using this template:

    ## `<callable>(<parameters>)`

    <One sentence on what the callable returns or does.>

    Source: <docstring, comment, or requirement>.

    | <parameter> | expected                         | note     |
    | ----------- | -------------------------------- | -------- |
    | <value>     | <exact return value>             | boundary |
    | <value>     | raises <Error>: "<full message>" | error    |

- Add one column per parameter. For stateful code, add a `given` column
  first to record the starting state.
- One row per case. Write boundaries as concrete rows on both sides,
  never as ranges.
- Start each note with happy, boundary, edge, or error.
- Mark values inferred only from the implementation as NEEDS REVIEW.
