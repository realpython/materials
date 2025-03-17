from textual.app import App
from textual.widgets import Button, Input


class ButtonsAndInputsApp(App):
    def compose(self):
        # Buttons
        yield Button("Click me!")
        yield Button("Primary!", variant="primary")
        yield Button.success("Success!")
        yield Button.warning("Warning!")
        yield Button.error("Error!")
        # Inputs
        yield Input(placeholder="Type your text here")
        yield Input(placeholder="Password", password=True)
        yield Input(
            placeholder="Type a number here",
            type="number",
            tooltip="Digits only please!",
        )


if __name__ == "__main__":
    app = ButtonsAndInputsApp()
    app.run()
