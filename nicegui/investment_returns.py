import re

from nicegui import app, ui


def investment_returns(principal, rate, term, interest_type):
    if interest_type == "Simple":
        return principal + (principal * rate / 100 * term)
    elif interest_type == "Compound":
        return principal * (pow((1 + rate / 100), term))


regexp = r"^[+]?[0-9]+$"

ui.page_title("Investment Calculator")

with ui.grid(columns=2):

    ui.label("Investment Principal ($):")
    principal = ui.input(
        value=1000,
        validation=lambda value: (
            "Positive Whole Amounts Only"
            if not re.search(regexp, value)
            else None
        ),
    )

    ui.label("Interest Payment:")
    interest_type = ui.toggle(["Simple", "Compound"], value="Simple")

    ui.label("Investment Term (Years):")
    term = ui.select([1, 2, 3], value=1)

    ui.label("Expected Growth (%):")
    rate = ui.radio([5, 7.5, 10], value=5)

    returns = ui.label("")
    calculate_return = ui.button(
        text="Total Expected Returns",
        on_click=lambda: returns.set_text(
            f"Expected Return: ${investment_returns(
                int(principal.value), float(rate.value),
                int(term.value), str(interest_type.value)):,.2f}"
        ),
    )

ui.button(text="logout", on_click=app.shutdown)

ui.run()
