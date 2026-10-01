from nicegui import ui

with ui.row().classes("w-full items-center gap-4 p-4"):
    ui.icon("request_quote", size="md").props("color=primary")
    ui.label("Estimate").classes("text-h6 text-weight-bold")

with ui.card().classes("w-80"):
    quantity = ui.number("Quantity", value=2, min=1)
    unit_price = ui.number("Unit price", value=40.0, min=0, format="%.2f")
    taxed = ui.checkbox("Add 20% tax")
    total = ui.label("Total: —").classes("text-subtitle1")

    def calculate() -> None:
        qty = quantity.value
        price = unit_price.value
        if qty is None or price is None or qty < 1 or price < 0:
            total.set_text("Total: —")
            ui.notify("Enter a quantity and a unit price", type="warning")
            return

        amount = float(qty) * float(price)
        if taxed.value:
            amount *= 1.2
        total.set_text(f"Total: {amount:.2f}")

    ui.button("Calculate", on_click=calculate).props("color=primary")

ui.run()
