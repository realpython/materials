import secrets
import string

from nicegui import ui

length = ui.number("Length", value=16, min=8, max=64)
digits = ui.checkbox("Include digits", value=True)
symbols = ui.checkbox("Include symbols")
password = ui.input("Password").props("readonly")
status = ui.label("Click Generate for a new password.")


def generate() -> None:
    size = length.value
    if (
        size is None
        or size != int(size)
        or size < 8
        or size > 64
    ):
        password.set_value("")
        status.set_text("Choose a whole length from 8 to 64.")
        ui.notify("Length must be a whole number from 8 to 64", type="warning")
        return

    alphabet = string.ascii_letters
    if digits.value:
        alphabet += string.digits
    if symbols.value:
        alphabet += "!@#$%^&*()-_=+"

    size = int(size)
    result = "".join(secrets.choice(alphabet) for _ in range(size))
    password.set_value(result)
    status.set_text(f"Generated a {size}-character password.")


ui.button("Generate", on_click=generate)

ui.run(native=True)