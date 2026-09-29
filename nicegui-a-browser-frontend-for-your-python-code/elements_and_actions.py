from nicegui import ui

name = ui.input("Name", value="Ada")
count = ui.number("Copies", value=2, min=1, max=10)
out = ui.label()


def run() -> None:
    out.set_text(f"Hello, {name.value}! ({int(count.value)} copies)")


ui.button("Run", on_click=run)
ui.run()
