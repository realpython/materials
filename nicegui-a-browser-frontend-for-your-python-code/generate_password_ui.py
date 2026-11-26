from nicegui import ui

from generate_password_cli import (
    DEFAULT_LENGTH,
    MAX_LENGTH,
    MIN_LENGTH,
    generate_password,
)


def generate() -> None:
    size = length.value
    if size is None:
        show_error("Enter a length.")
        return
    if not float(size).is_integer():
        show_error("Enter a whole number for the length.")
        return

    try:
        result = generate_password(int(size), digits.value, symbols.value)
    except ValueError as error:
        show_error(f"{str(error).capitalize()}.")
        return

    password.set_value(result)
    status.set_text(f"Generated a new password with {int(size)} characters.")


def show_error(message: str) -> None:
    password.set_value("")
    status.set_text(message)
    ui.notify(message, type="warning")


length = ui.number(
    "Length",
    value=DEFAULT_LENGTH,
    min=MIN_LENGTH,
    max=MAX_LENGTH,
)
digits = ui.checkbox("Allow digits", value=True)
symbols = ui.checkbox("Allow symbols")
password = ui.input("Password").props("readonly").classes("w-full")
status = ui.label("Click Generate for a new password.")
ui.button("Generate", on_click=generate)

ui.run()
