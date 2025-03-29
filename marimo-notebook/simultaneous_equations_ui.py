import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    equation_1_x = mo.ui.text(value="-3.5")
    equation_1_y = mo.ui.text(value="7")
    equation_2_x = mo.ui.text(value="7")
    equation_2_y = mo.ui.text(value="-10")
    equation_1_result = mo.ui.text(value="0")
    equation_2_result = mo.ui.text(value="4")

    mo.md(
        f"""
        Enter your equation's coefficients below:

        {equation_1_x}$x$ + {equation_1_y}$y$ = {equation_1_result}

        {equation_2_x}$x$ + {equation_2_y}$y$ = {equation_2_result}
        """
    )
    return (
        equation_1_result,
        equation_1_x,
        equation_1_y,
        equation_2_result,
        equation_2_x,
        equation_2_y,
    )


@app.cell
def _(
    equation_1_result,
    equation_1_x,
    equation_1_y,
    equation_2_result,
    equation_2_x,
    equation_2_y,
):
    import numpy as np

    coefficients = np.array(
        [
            [float(equation_1_x.value), float(equation_1_y.value)],
            [float(equation_2_x.value), float(equation_2_y.value)],
        ]
    )
    results = np.array(
        [float(equation_1_result.value), float(equation_2_result.value)]
    )
    solution = np.linalg.solve(coefficients, results)
    return coefficients, np, results, solution


@app.cell
def _(
    equation_1_result,
    equation_1_x,
    equation_1_y,
    equation_2_result,
    equation_2_x,
    equation_2_y,
    mo,
    solution,
):
    mo.md(
        f"""
        The solution to the simultaneous equations:

        **{float(equation_1_x.value):.2f}$x${float(equation_1_y.value):+.2f}$y$ = {equation_1_result.value}**

        **{float(equation_2_x.value):.2f}$x${float(equation_2_y.value):.2f}$y$ = {equation_2_result.value}**

        is

        **$x$ = {solution[0]}**
        **$y$ = {solution[1]}**
        """
    )
    return


if __name__ == "__main__":
    app.run()
