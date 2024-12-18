from itertools import cycle

from textual import on
from textual.app import App
from textual.containers import Container, Horizontal
from textual.widgets import Button, Input, Label, Digits

COLORS = cycle(["red", "green", "orange", "blue", "yellow"])


class ButtonsAndInputsApp(App):
    CSS_PATH = "buttons_and_inputs.tcss"
    BUTTON_PRESSES = 0

    def compose(self):
        with Horizontal():
            yield Button(
                "Click me!",
                id="colorbutton",
                tooltip="I change the label colors\nand update the counter",
            )
            yield Input(
                placeholder="Type here", tooltip="I change the label text"
            )
        with Horizontal():
            label = Label("Hello, Textual!", id="mainlabel")
            label.border_title = "You can change this label"
            yield label
            digits_container = Container()
            digits_container.border_title = "Button counter"
            with digits_container:
                yield Digits("0", id="digits")

    @on(Button.Pressed)
    def change_label_style(self, event):
        self.BUTTON_PRESSES += 1
        mainlabel = self.query_one("#mainlabel")
        mainlabel.styles.color = next(COLORS)
        mainlabel.styles.border_title_color = next(COLORS)
        digits = self.query_one("#digits")
        digits.update(f"{self.BUTTON_PRESSES}")

    @on(Input.Changed)
    def change_label_text(self, event):
        mainlabel = self.query_one("#mainlabel")
        mainlabel.update(event.value)


if __name__ == "__main__":
    app = ButtonsAndInputsApp()
    app.run()
