import re

from nicegui import app, ui


def investment_returns(principal, rate, term, interest_type):
    if interest_type == "Simple":
        return principal + (principal * rate / 100 * term)
    elif interest_type == "Compound":
        return principal * (pow((1 + rate / 100), term))


regexp = r"^[+]?[0-9]+$"

ui.query("body").style("background-color: lavender")

ui.page_title("Investment Calculator")
ui.html("<b><i><h6>Select your investment options:</h6></i></b>")

with ui.grid(columns=2).classes("border p-4 items-center"):

    ui.label("Investment Principal ($):").classes("font-bold")
    principal = ui.input(
        value=1000,
        validation=lambda value: (
            "Positive Whole Amounts Only"
            if not re.search(regexp, value)
            else None
        ),
    )

    ui.label("Interest Payment:").classes("font-bold")
    interest_type = ui.toggle(["Simple", "Compound"], value="Simple")

    ui.label("Investment Term (Years):").classes("font-bold")
    term = ui.select([1, 2, 3], value=1)

    ui.label("Expected Growth (%):").classes("font-bold")
    rate = ui.radio([5, 7.5, 10], value=5).props("inline")

    returns = ui.label("Expected Return: $1,050.00").classes(
        "font-bold col-span-2 text-blue-600 text-center"
    )

    calculate_return = (
        ui.button(
            text="Total Expected Returns",
            on_click=lambda: returns.set_text(
                f"Expected Return: ${investment_returns(
                int(principal.value), float(rate.value),
                int(term.value), str(interest_type.value)):,.2f}"
            ),
            color="purple",
        )
        .tooltip("Calculate Returns")
        .classes("rounded-xl shadow-lg col-span-2")
    )

ui.button(
    icon="logout", on_click=app.shutdown, color="green"
).tooltip("Exit").props("round")

ui.run()
