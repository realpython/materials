# Marimo: A Reactive, Reproducible Notebook

The materials contained in this download are designed to complement the Real Python tutorial [Marimo: A Reactive, Reproducible Notebook](https://realpython.com/marimo-notebook/).

## Installation

Create a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/), activate it, and install marimo along with its dependencies into it:

```sh
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

## Contents

Your download bundle contains the following files:

| Filename                                   | Description                                                                                     |
|--------------------------------------------|-------------------------------------------------------------------------------------------------|
| `hypotenuse_calculator.py`                 | The original `hypotenuse_calculator` code.                                     |
| `hypotenuse_calculator_before_update.py`   | The code before any updating is attempted. The code is out of order but runs cleanly. |
| `hypotenuse_calculator_duplicate_variable.py` | Shows the effect of redefining a variable. This file produces an error.              |
| `hypotenuse_calculator_after_update.py`    | The code after the `adjacent` variable was updated to `10`. Runs cleanly.    |
| `hypotenuse_calculator_after_deletion.py`  | The code after the `opposite` variable was deleted. This file produces an error. |
| `break_even_analysis_chart_code.py`        | The basic chart code for a break-even analysis with fixed input data.        |
| `break_even_analysis_ui_elements.py`       | Includes four UI interface elements to allow the plot to be adjusted.                 |
| `break_even_analysis_solution.py`          | A possible solution to the skills test.                                      |
| `packages.py`                              | The code used to demonstrate sandboxing.                                     |
| `quadratic.py`                             | The marimo notebook version of the quadratic formula example.                |
| `equation.py`                              | The Python script version of `quadratic.py`.                                 |
| `simultaneous_equations.py`               | The code used to demonstrate marimo's UI elements.                           |
| `simultaneous_equations_ui.py`            | A possible solution to the challenge skills test.                            |
| `hidden_state.ipynb`                       | This Jupyter Notebook is a starting point for investigating its problems, to be adjusted per tutorial. |
