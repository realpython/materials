# NiceGUI: A Browser Frontend for Your Python Code

Sample scripts that build small user interfaces with [NiceGUI](https://nicegui.io/). Each file is a complete app.

## Setup

These examples need Python 3.10 or newer. Create a virtual environment and install the dependencies:

```console
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

On Windows, activate the environment with `venv\Scripts\activate`.

`requirements.txt` installs NiceGUI 3.17.0 with the Plotly extra, along with pinned versions of Plotly, pandas, and [pywebview](https://pywebview.flowrl.com/). `hello_nicegui_native.py` uses pywebview to open a desktop window. On Linux, pywebview also needs a system WebKit or Qt backend. The [pywebview installation guide](https://pywebview.flowrl.com/guide/installation.html) lists the packages for each platform.

## Examples

| Script | What it shows |
| --- | --- |
| `hello_nicegui_browser.py` | A label and a button that shows a notification in the browser |
| `hello_nicegui_native.py` | The same interface in a native desktop window |
| `elements_and_actions.py` | Text and number inputs that update a label when you click Run |
| `layout_and_styling.py` | A row, a card, an icon, a badge, and Quasar utility classes |

Run an example from this folder:

```console
$ python hello_nicegui_browser.py
```

NiceGUI prints a local URL, usually `http://127.0.0.1:8080`. Open that address in a browser. Stop the app with Ctrl+C.

The native example opens its own window:

```console
$ python hello_nicegui_native.py
```
