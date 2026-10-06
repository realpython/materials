---
name: extract-behavior
description: Extracts the intended behavior of a Python module or package
  into BEHAVIOR.md as reviewable tables. Use before writing tests.
argument-hint: <path/to/module.py | path/to/package/>
disable-model-invocation: true
---

# Extract Behavior

Extract the intended behavior of `$ARGUMENTS` into `BEHAVIOR.md`.

## Steps

1. Collect the target modules:
   - If `$ARGUMENTS` is a `.py` file, the target is that module.
   - If it's a directory, the targets are all `.py` files under it,
     recursively, in path order. Skip tests, files whose names start
     with an underscore, `_`.
2. Carefully read the package that contains the targets and map it: list
   each module's public callables, their parameters, branches, error
   paths, and external dependencies.
3. For each target module, write its section group in `BEHAVIOR.md` at
   the project root. Start the group with a `` # `<module path>` ``
   heading, then write one section per public callable. Include every
   decision point, boundary, error, and edge case. Replace any existing
   group for the module, and leave the other groups alone.
4. Report the modules and sections you wrote, and every row marked
   NEEDS REVIEW.

Don't write tests or edit any code.

## Template

Use this template for every section:

    ## `<callable>(<parameters>)`

    <One sentence on what the callable returns or does.>

    Source: <docstring, comment, or requirement>.

    | <parameter> | expected                         | note     |
    | ----------- | -------------------------------- | -------- |
    | <value>     | <exact return value>             | boundary |
    | <value>     | raises <Error>: "<full message>" | error    |

## Rules

- Add one column per parameter. For stateful code, add a `given` column
  first to record the starting state.
- One row per case. Write boundaries as concrete rows on both sides,
  never as ranges.
- Start each note with happy, boundary, edge, or error.
- Mark values inferred only from the implementation as NEEDS REVIEW.
