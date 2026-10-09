# NiceGUI: A Browser Frontend for Your Python Code

Sample scripts for the Real Python NiceGUI tutorial. Each NiceGUI file is a complete app. `generate_password_cli.py` is a plain CLI helper used by the password UI example.

## Setup

These examples need **Python 3.11 or later**. Create a virtual environment and install the dependencies:

```console
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

On Windows, activate the environment with `venv\Scripts\activate`.

`requirements.txt` installs NiceGUI 3.17.0 with the Plotly extra, along with pinned versions of Plotly, pandas, and [pywebview](https://pywebview.flowrl.com/). `hello_nicegui_native.py` uses pywebview to open a desktop window. On Linux, install a GTK backend as in the tutorial (`pywebview[gtk]` plus the system libraries from the [pywebview installation guide](https://pywebview.flowrl.com/guide/installation.html)).

## Examples

| Script | What it shows |
| --- | --- |
| `hello_nicegui.py` | Minimal label and button in the browser |
| `hello_nicegui_native.py` | Same app in a native desktop window (`native=True`) |
| `element_catalog.py` | Common inputs and a summary label |
| `generate_password_cli.py` | CLI password generator |
| `generate_password_ui.py` | Browser UI that calls the CLI function |
| `estimate_card.py` | Layout, styling, and a custom color palette |
| `request_chart.py` | Built-in ECharts bar chart and table |
| `plotly_chart.py` | Plotly bar chart from a pandas DataFrame |

Run a NiceGUI example from this folder:

```console
$ python hello_nicegui.py
```

NiceGUI prints a local URL, usually `http://127.0.0.1:8080`. Open that address in a browser. Stop the app with Ctrl+C.

The native example opens its own window:

```console
$ python hello_nicegui_native.py
```

The password CLI works without starting a server:

```console
$ python generate_password_cli.py -l 24 --symbols
```
