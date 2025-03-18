import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    oimport marimo as mo
    """,
    name="_",
)


@app.cell
def _(
    ui_color_costs,
    ui_fixed_cost,
    ui_quantity,
    ui_selling_price,
    ui_unit_cost,
):
    import matplotlib.pyplot as plt

    fixed_cost = int(ui_fixed_cost.value)
    unit_cost = ui_unit_cost.value
    selling_price = float(ui_selling_price.value)
    upper_production_quantity = ui_quantity.value

    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = break_even_quantity * selling_price

    units = range(0, upper_production_quantity + 1, 1000)
    unit_costs = [(unit * unit_cost) + fixed_cost for unit in units]
    sales_income = [unit * selling_price for unit in units]

    plt.plot(units, unit_costs, marker="o", color=ui_color_costs.value)
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
        fixed_cost,
        plt,
        sales_income,
        selling_price,
        unit_cost,
        unit_costs,
        units,
        upper_production_quantity,
    )


@app.cell
def _(mo):
    options = ["40000", "50000"]
    ui_fixed_cost = mo.ui.radio(options=options, value="50000")

    ui_unit_cost = mo.ui.slider(start=2, stop=5, step=1)

    ui_selling_price = mo.ui.text(value="10")

    ui_quantity = mo.ui.dropdown(
        options={"10000": 10000, "12000": 12000, "15000": 15000}, value="10000"
    )

    ui_disply_break_even = mo.ui.switch()

    ui_color_costs = mo.ui.dropdown(
        options={"Red": "red", "Green": "green", "Blue": "blue"}, value="Red"
    )

    mo.md(
        f"""
        Select Fixed Costs: {ui_fixed_cost}

        Select Unit Cost Price: {ui_unit_cost}

        Enter Selling Price: {ui_selling_price}

        Select a Maximum Production Quantity: {ui_quantity}
        """
    )
    return (
        options,
        ui_color_costs,
        ui_disply_break_even,
        ui_fixed_cost,
        ui_quantity,
        ui_selling_price,
        ui_unit_cost,
    )


if __name__ == "__main__":
    app.run()
