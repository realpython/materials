import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt

    fixed_cost = 50000
    unit_cost = 2
    selling_price = 10
    unit_range = 10

    break_even_quantity = fixed_cost / (selling_price - unit_cost)
    break_even_income = fixed_cost + break_even_quantity * unit_cost

    units = [x * 1000 for x in range(unit_range)]
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
        fixed_cost,
        plt,
        sales_income,
        selling_price,
        unit_cost,
        unit_costs,
        unit_range,
        units,
    )


if __name__ == "__main__":
    app.run()
