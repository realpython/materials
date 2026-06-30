# Validating Data With Pointblank in Python

Supporting code and sample data for the Real Python tutorial
"Validating Data With Pointblank in Python".

## Requirements

The Python scripts use PEP 723 dependency metadata and run with
[uv](https://docs.astral.sh/uv/):

```console
$ uv run pointblank_quickstart.py
$ uv run pointblank_thresholds.py
$ uv run pointblank_atoms.py
```

The command-line examples can run without a project environment:

```console
$ uv run --no-project --with 'pointblank[pl]' -- pb scan pointblank_atoms.csv
$ uv run --no-project --with 'pointblank[pl]' -- pb missing pointblank_atoms.csv
$ uvx --from 'pointblank[pl]' pb run pointblank_atoms.yaml --output-html pointblank_report.html
```

