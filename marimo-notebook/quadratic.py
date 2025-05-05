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
        A quadratic equation is one of the form **$ax^2 + bx + c = 0$**, where a, b and c are constants, and a $\neq$ 0.

        You can solve it using the *quadratic formula*:

        $$x = \frac {-b \pm \sqrt{b^2 -4ac}} {2a}$$

        For example, suppose you wanted to solve: **$2x^2 - 3x - 2 = 0$**
        """
    )
    return


@app.cell
def _(a, b, c, math):
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x1,)


@app.cell
def _(a, b, c, math):
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return (x2,)


@app.cell
def _():
    a = 2
    return (a,)


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _():
    b = -3
    return (b,)


@app.cell
def _():
    c = -2
    return (c,)


@app.cell
def _(x1, x2):
    print(f"x = {x1} and {x2}.")
    return


if __name__ == "__main__":
    app.run()
