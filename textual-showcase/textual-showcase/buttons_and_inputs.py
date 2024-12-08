from itertools import cycle

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Input, Label

COLORS = cycle(["red", "green", "orange", "blue", "yellow"])


class ButtonsAndInputsApp(App):
    CSS_PATH = "buttons_and_inputs.tcss"
    BUTTON_PRESSES = 0

    def compose(self) -> ComposeResult:
        # Add widgets to the app
        with Horizontal():
            yield Button(
                "Click me!",
                id="colorbutton",
                tooltip="I change the label colors",
            )
            yield Input(
                placeholder="Type here", tooltip="I change the label text"
            )
        with Horizontal():
            label = Label("Hello, Textual!", id="mainlabel")
            label.border_title = "You can change this label"
            yield label
            countinglabel = Label("Press a button", id="countinglabel")
            countinglabel.border_title = "Button counter"
            yield countinglabel

    @on(Button.Pressed)
    def change_label_style(self, event):
        self.BUTTON_PRESSES += 1
        mainlabel = self.query_one("#mainlabel")
        countinglabel = self.query_one("#countinglabel")
        mainlabel.styles.color = next(COLORS)
        mainlabel.styles.border_title_color = next(COLORS)
        countinglabel.update(f"Button pressed {self.BUTTON_PRESSES} times")

    @on(Input.Changed)
    def change_label_text(self, event):
        mainlabel = self.query_one("#mainlabel")
        mainlabel.update(event.value)


if __name__ == "__main__":
    app = ButtonsAndInputsApp()
    app.run()
