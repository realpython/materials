# NiceGUI: A Browser Frontend for Your Python Code

Sample scripts that build small user interfaces with [NiceGUI](https://nicegui.io/). Each NiceGUI file is a complete app. `csv_to_markdown.py` is a plain CLI helper used by the UI example.

## Setup

These examples need Python 3.10 or newer. Create a virtual environment and install the dependencies:

```console
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

On Windows, activate the environment with `venv\Scripts\activate`.

`requirements.txt` installs NiceGUI 3.17.0 with the Plotly extra, along with pinned versions of Plotly, pandas, and [pywebview](https://pywebview.flowrl.com/). `password_generator_native.py` uses pywebview to open a desktop window. On Linux, pywebview also needs a system WebKit or Qt backend. The [pywebview installation guide](https://pywebview.flowrl.com/guide/installation.html) lists the packages for each platform.

## Examples

| Script | What it shows |
| --- | --- |
| `element_catalog.py` | Common inputs (text, number, select, checkbox, radio, slider, switch) and a summary label |
| `estimate_card.py` | A card with quantity, unit price, optional tax, and a calculated total |
| `password_generator.py` | A password generator in the browser |
| `password_generator_native.py` | The same password generator in a native desktop window |
| `csv_to_markdown.py` | CLI that converts a CSV file to a Markdown table |
| `csv_to_markdown_ui.py` | Browser UI for the converter, with progress and `run.io_bound` |
| `request_chart.py` | An ECharts bar chart and a table of request counts |
| `plotly_chart.py` | A Plotly bar chart from a pandas DataFrame |

Run a NiceGUI example from this folder:

```console
$ python password_generator.py
```

NiceGUI prints a local URL, usually `http://127.0.0.1:8080`. Open that address in a browser. Stop the app with Ctrl+C.

The native example opens its own window:

```console
$ python password_generator_native.py
```

The CLI converter works without starting a server:

```console
$ python csv_to_markdown.py people.csv
```
