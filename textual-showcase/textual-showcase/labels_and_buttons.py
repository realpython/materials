from itertools import cycle

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Label

COLORS = cycle(["red", "green", "orange","blue", "yellow"])
DOCKS = cycle(["top","bottom"])


class LabelsAndButtonsApp(App):
    CSS_PATH = "labels_and_buttons.tcss"
    BUTTON_PRESSES = 0
 
    def compose(self) -> ComposeResult:
        # Add widgets to the app
        with Horizontal():
            yield Button("I change the colors", id="colorbutton")
            yield Button("I change the layout", id="layoutbutton")
        label = Label("Hello, Textual!", id="mainlabel")
        label.border_title = "Change this label"
        yield label

    @on(Button.Pressed)
    def change_label(self, event):
        self.BUTTON_PRESSES += 1
        label = self.query_one("#mainlabel")
        if event.button.id == "colorbutton":
            label.styles.color = next(COLORS)
            label.styles.border_title_color = next(COLORS)
        elif event.button.id == "layoutbutton":
            label.styles.dock = next(DOCKS)
        label.update(f"There have been {self.BUTTON_PRESSES} button clicks")


if __name__ == "__main__":
    app = LabelsAndButtonsApp()
    app.run()
