from nicegui import ui

name = ui.input("Project", value="notes")
notes = ui.textarea("Notes", value="Ship the export")
copies = ui.number("Copies", value=2, min=1, max=10)
kind = ui.select(["Draft", "Final"], value="Draft", label="Kind")
urgent = ui.checkbox("Urgent")
ui.label("Extension")
extension = ui.radio(["txt", "csv"], value="txt")
ui.label("Priority")
priority = ui.slider(min=0, max=10, value=3)
archive = ui.switch("Archive after")
summary = ui.label("No choices yet")


def show() -> None:
    summary.set_text(
        f"{name.value}: {kind.value}.{extension.value}, "
        f"copies={copies.value}, urgent={urgent.value}, "
        f"priority={priority.value}, archive={archive.value}"
    )
    if notes.value:
        ui.notify(notes.value)


ui.button("Show choices", on_click=show)

ui.run()
