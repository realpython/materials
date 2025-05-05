import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        **Problem:**

        Solve the following simultaneous equations using Python:

        $4x + 2y = 34$

        $2x - y = 31$
        """
    )
    return


@app.cell
def _():
    import numpy as np

    coefficients = np.array([[4, 2], [2, -1]])
    results = np.array([34, 31])
    solution = np.linalg.solve(coefficients, results)
    solution
    return coefficients, np, results, solution


@app.cell
def _(mo, solution):
    mo.md(
        f"""
        The solution to these simultaneous equations is:

        **x = {solution[0]}**

        **y = {solution[1]}**
        """
    )
    return


if __name__ == "__main__":
    app.run()
