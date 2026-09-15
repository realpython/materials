# Positron IDE: A Hands-on Python Tutorial

Sample code for the Real Python tutorial [Positron IDE: A Hands-on Python Tutorial](https://realpython.com/positron-ide/).

## Setup

Open this folder in Positron and run the following command in its terminal:

```console
uv sync --locked
```

Select the project's `.venv` for both the Python Console and the notebook kernel. The project uses Python 3.14 and pins its starting dependencies in `pyproject.toml` and `uv.lock`.

## Prepare and Analyze the Data

Run `src/prepare_sales.py` cell by cell in Positron, or run it from this folder:

```console
uv run src/prepare_sales.py
```

Positron's Console starts at the project root, so the scripts set `PROJECT_ROOT = Path.cwd()`. A notebook kernel starts in the notebook's own folder instead, so `notebooks/explore_sales.ipynb` uses `Path.cwd().parent`.

This creates `data/sales_clean.csv`. It checks for missing values, duplicates, and inconsistent totals, corrects a column name, parses dates, and normalizes category labels. It preserves all 5,130 source rows.

Next, run the cells in `src/analyze_sales.py` to inspect descriptive statistics, compare median order values between retail and wholesale orders, and view a Matplotlib chart. Use Positron's **Run Cell** controls to keep the resulting objects available in the Console and Variables pane.

## Run the Notebook

Open `notebooks/explore_sales.ipynb` and run its cells in order. The notebook covers the same ground as both scripts, from loading the raw CSV through cleaning, describing, grouping, and charting the data. It creates its own variables independently of the Console session, so you can run it without running the scripts first.

Before running the Plotly cell, add its dependency from this folder:

```console
uv add plotly==7.0.0
```

This updates the environment, `pyproject.toml`, and `uv.lock`. If you restart the notebook kernel afterward, rerun the preceding cells. Plotly is intentionally absent from the starting dependencies so you can follow the tutorial's package-management demonstration.

Posit Assistant is optional. It requires connecting a supported model provider, and no AI account is needed to run the examples.

## Dataset

The fictional sales data is reused from Real Python's [pandas pivot-table materials](https://github.com/realpython/materials/tree/master/pandas-pivot-table). See [data/README.md](data/README.md) for its original source and attribution and [data/LICENSE-2.0.txt](data/LICENSE-2.0.txt) for the Apache 2.0 license.
