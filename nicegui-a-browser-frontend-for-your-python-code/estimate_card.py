from nicegui import ui

ui.colors(
    primary="#0F766E",
    secondary="#334155",
    accent="#C2410C",
)

with ui.row().classes("w-full items-center gap-4 p-4"):
    ui.icon("request_quote", size="md").props("color=primary")
    ui.label("Estimate").classes("text-h6 text-weight-bold")
    ui.space()
    ui.badge("Draft").props("color=secondary")

with ui.card().classes("w-80 shadow-2"):
    ui.label("Line item").classes("text-subtitle2 text-weight-medium")
    quantity = ui.number("Quantity", value=2, min=1).classes("w-full")
    unit_price = ui.number(
        "Unit price", value=40.0, min=0, format="%.2f"
    ).classes("w-full")
    taxed = ui.checkbox("Add 20% tax")
    ui.separator()
    total = ui.label("Total: —").classes("text-h6 text-weight-bold")
    ui.label("Tax is off by default.").classes("text-caption text-grey-7")

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

    ui.button("Calculate", on_click=calculate).props(
        "color=primary"
    ).classes("w-full q-mt-md")

ui.run()
