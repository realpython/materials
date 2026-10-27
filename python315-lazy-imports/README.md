# Python 3.15 Preview: Lazy Imports

This folder provides the code examples for the Real Python tutorial [Python 3.15 Preview: Lazy Imports](https://realpython.com/python315-lazy-imports/)

Everything here is standard library only, but it needs **Python 3.15** or later, because most of the files use the `lazy` keyword from [PEP 810](https://peps.python.org/pep-0810/). On earlier versions those files raise a `SyntaxError` before they run.

## What's Here

| Path | Section |
| --- | --- |
| `noisy_module.py`, `probe.py` | Defer a Whole Module |
| `shapes.py`, `partial.py` | Defer a Name From a Module |
| `badfunc.py` | Find Out Where `lazy` Isn't Allowed |
| `report_cli/` | Speed Up a Real CLI |
| `type_checking_guard.py`, `lazy_annotation.py` | Retire the `if TYPE_CHECKING` Dance |
| `fail.py` | Read a Deferred Import Error |
| `circular/` | Don't Expect a Circular Import Fix |
| `bridge.py`, `allmode.py` | Go Lazy Without the Keyword |

## The Report CLI

`report_cli/` holds three versions of the same command-line tool:

- `cli_eager.py` imports everything eagerly.
- `cli_lazy.py` marks five heavy standard library imports `lazy` and is otherwise identical.
- `cli_too_lazy.py` also defers the two plug-in imports, which silently empties the format registry.

Run the benchmark from inside that folder:

```console
$ python bench.py cli_eager.py --help
$ python bench.py cli_lazy.py --help
```

The `--load-all` flag reads all five deferred names, so you can check that deferral costs nothing once the modules are actually used.

## Circular Imports

Each subfolder of `circular/` is self-contained. Run `python main.py` from inside it:

- `eager/` — a two-module cycle that fails.
- `lazy/` — the same cycle with one import deferred, which fixes it.
- `init_eager/` and `init_lazy/` — a cycle that needs a value during module initialization, which deferral does not fix. Both fail with the same `ImportError`.

## Files That Fail on Purpose

Three files here are meant to raise. If you run them and see a traceback, that's the point:

- `badfunc.py` — `SyntaxError`, because `lazy` isn't allowed inside a function.
- `fail.py` — a chained `ImportError` from a deferred import of a module that doesn't exist.
- `type_checking_guard.py` — `NameError`, which is the problem the lazy version solves.

The `circular/eager/`, `circular/init_eager/`, and `circular/init_lazy/` folders fail on purpose too.

## Getting a 3.15 With tkinter

`report_cli/cli_eager.py` imports `tkinter` at module level, because it's the heaviest import in the demo. A `uv`-managed 3.15 has it. If you build 3.15 with `pyenv` instead, install your platform's Tk development headers first, or the build produces an interpreter without `tkinter` and the CLI won't start.

## Note on Formatting

These files follow the Real Python style guide's blank-line rules rather than PEP 8, so they're excluded from the repository's `ruff` checks. `ruff` also can't parse the `lazy` keyword yet.
