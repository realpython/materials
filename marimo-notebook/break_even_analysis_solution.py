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
def _(ui_fixed_cost, ui_quantity, ui_selling_price, ui_unit_cost):
    fixed_cost = int(ui_fixed_cost.value)
    unit_cost = ui_unit_cost.value
    selling_price = float(ui_selling_price.value)
    upper_production_quantity = ui_quantity.value
    return fixed_cost, selling_price, unit_cost, upper_production_quantity


@app.cell
def _(
    fixed_cost,
    plt,
    selling_price,
    ui_break_even,
    ui_plot_color,
    unit_cost,
    upper_production_quantity,
):
    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = break_even_quantity * selling_price

    units = range(0, upper_production_quantity + 1, 1000)
    total_costs = [(unit * unit_cost) + fixed_cost for unit in units]
    sales_income = [unit * selling_price for unit in units]

    plt.plot(units, total_costs, marker="o", color=ui_plot_color.value)
    plt.plot(units, sales_income, marker="x")

    plt.xlabel("Units Produced")
    plt.ylabel("($)")
    plt.legend(["Total Costs", "Total Income"])
    plt.title("Break-Even Analysis")

    if ui_break_even.value:
        plt.vlines(
            break_even_quantity,
            ymin=100,
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
        total_costs,
        units,
    )


@app.cell
def _(mo):
    ui_fixed_cost = mo.ui.radio(options=["40000", "50000"], value="50000")

    ui_unit_cost = mo.ui.slider(start=2, stop=5, step=1)

    ui_selling_price = mo.ui.text(value="10")

    ui_quantity = mo.ui.dropdown(
        options={"10000": 10000, "12000": 12000, "15000": 15000}, value="10000"
    )

    ui_break_even = mo.ui.switch()

    ui_plot_color = mo.ui.dropdown(
        options={"Red": "red", "Green": "green", "Blue": "blue"}, value="Red"
    )

    mo.md(
        f"""
        Fixed Costs: {ui_fixed_cost}

        Unit Cost Price: {ui_unit_cost}

        Selling Price: {ui_selling_price}

        Maximum Quantity: {ui_quantity}

        Display Break-Even Data: {ui_break_even}

        Total Costs Plot Color: {ui_plot_color}
        """
    )
    return (
        ui_break_even,
        ui_fixed_cost,
        ui_plot_color,
        ui_quantity,
        ui_selling_price,
        ui_unit_cost,
    )


if __name__ == "__main__":
    app.run()
