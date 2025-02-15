import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(
    drop_color_costs,
    drop_quantity,
    rd_fixed_cost,
    sl_cost_price,
    text_selling_price,
):
    import matplotlib.pyplot as plt

    fixed_cost = int(rd_fixed_cost.value)
    unit_cost = sl_cost_price.value
    selling_price = float(text_selling_price.value)
    upper_production_quantity = drop_quantity.value

    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = break_even_quantity * selling_price

    units = [
        quantity * 1000 for quantity in range(upper_production_quantity + 1)
    ]
    unit_costs = [(unit * unit_cost) + fixed_cost for unit in units]
    sales_income = [unit * selling_price for unit in units]

    plt.plot(units, unit_costs, marker="o", color=drop_color_costs.value)
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
    rd_fixed_cost = mo.ui.radio(options=options, value="50000")

    sl_cost_price = mo.ui.slider(start=2, stop=5, step=1)

    text_selling_price = mo.ui.text(value="10")

    drop_quantity = mo.ui.dropdown(
        options={"10000": 10, "12000": 12, "15000": 15}, value="10000"
    )

    sw_disply_break_even = mo.ui.switch()

    drop_color_costs = mo.ui.dropdown(
        options={"Red": "red", "Green": "green", "Blue": "blue"}, value="Red"
    )

    mo.md(
        f"""
        Select Fixed Costs: {rd_fixed_cost}

        Select Unit Cost Price: {sl_cost_price}

        Enter Selling Price: {text_selling_price}

        Select a Maximum Quantity: {drop_quantity}
        """
    )
    return (
        drop_color_costs,
        drop_quantity,
        options,
        rd_fixed_cost,
        sl_cost_price,
        sw_disply_break_even,
        text_selling_price,
    )


if __name__ == "__main__":
    app.run()
