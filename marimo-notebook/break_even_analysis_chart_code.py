# flake8: noqa

import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import marimo as mo
    return mo, plt


@app.cell
def _():
    fixed_cost = 50000
    unit_cost = 2
    selling_price = 10
    upper_production_quantity = 10000
    return fixed_cost, selling_price, unit_cost, upper_production_quantity


@app.cell
def _(
    fixed_cost,
    plt,
    selling_price,
    unit_cost,
    upper_production_quantity,
):
    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = fixed_cost + break_even_quantity * unit_cost

    units = range(0, upper_production_quantity + 1, 1000)
    unit_costs = [(x * unit_cost) + fixed_cost for x in units]
    sales_income = [unit * selling_price for unit in units]

    plt.plot(units, unit_costs, marker="o")
    plt.plot(units, sales_income, marker="x")

    plt.xlabel("Units Produced")
    plt.ylabel("($)")
    plt.legend(["Total Costs", "Total Income"])
    plt.title("Break-Even Analysis")

    plt.vlines(
        break_even_quantity,
        ymin=0,
        ymax=break_even_income,
        linestyles="dashed",
    )
    plt.text(
        x=break_even_quantity + 100,
        y=int(break_even_income / 2),
        s=int(break_even_quantity),
    )
    plt.grid()
    plt.show()
    return (
        break_even_income,
        break_even_quantity,
        sales_income,
        unit_costs,
        units,
    )


if __name__ == "__main__":
    app.run()
