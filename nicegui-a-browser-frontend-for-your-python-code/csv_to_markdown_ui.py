from nicegui import run, ui

from csv_to_markdown import csv_to_markdown

SAMPLE = "name,role\nAda,Engineer\nGrace,Scientist\n"

source = ui.textarea("CSV", value=SAMPLE).classes("w-full").props("rows=8")
delimiter = ui.select(
    {",": "Comma", ";": "Semicolon", "\t": "Tab"},
    value=",",
    label="Delimiter",
)
header = ui.checkbox("First row is the header", value=True)
status = ui.label("Paste CSV, then click Convert.")
progress = ui.linear_progress(show_value=False, size="8px").props(
    "indeterminate"
)
progress.set_visibility(False)
markdown = ui.textarea("Markdown").classes("w-full").props("rows=8")


async def convert() -> None:
    raw = source.value or ""
    convert_button.disable()
    progress.set_visibility(True)
    status.set_text("Converting")
    try:
        result = await run.io_bound(
            csv_to_markdown,
            raw,
            delimiter=delimiter.value,
            header=header.value,
        )
    except ValueError as exc:
        markdown.set_value("")
        status.set_text(str(exc))
        ui.notify(str(exc), type="negative")
        return
    finally:
        progress.set_visibility(False)
        convert_button.enable()

    markdown.set_value(result)
    status.set_text("Conversion complete.")
    ui.notify("Markdown table ready", type="positive")


convert_button = ui.button("Convert", on_click=convert)

ui.run()
