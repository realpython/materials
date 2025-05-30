import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell
def _(math):
    def calculate_hypotenuse(opposite, adjacent):
        return math.sqrt(opposite**2 + adjacent**2)

    return (calculate_hypotenuse,)


@app.cell
def _():
    opposite = 3
    return (opposite,)


@app.cell
def _():
    adjacent = 4
    return (adjacent,)


@app.cell
def _(adjacent, calculate_hypotenuse, opposite):
    calculate_hypotenuse(opposite, adjacent)
    return


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _():
    adjacent = 10
    return (adjacent,)


if __name__ == "__main__":
    app.run()
