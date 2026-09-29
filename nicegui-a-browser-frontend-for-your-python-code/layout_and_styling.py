from nicegui import ui

with ui.row().classes("w-full items-center gap-4 p-4"):
    ui.icon("dashboard", size="md").props("color=primary")
    ui.label("Ops Panel").classes("text-h6 text-weight-bold")

with ui.card().classes("w-80"):
    ui.label("Status").classes("text-subtitle2")
    ui.badge("Ready").props("color=positive")
    ui.button("Ping", on_click=lambda: ui.notify("Ready"))

ui.run()
