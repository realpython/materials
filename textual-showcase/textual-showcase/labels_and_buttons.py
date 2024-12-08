from itertools import cycle

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Input,  Label

COLORS = cycle(["red", "green", "orange", "blue", "yellow"])
DOCKS = cycle(["top", "right", "bottom", "left"])


class LabelsAndButtonsApp(App):
    CSS_PATH = "labels_and_buttons.tcss"
    BUTTON_PRESSES = 0

    def compose(self) -> ComposeResult:
        # Add widgets to the app
        with Horizontal():
            yield Button("I change the colors", id="colorbutton")
            yield Button("I change the layout", id="layoutbutton")
        yield Input(placeholder="Type here to change the label text")
        mainlabel = Label("Hello, Textual!", id="mainlabel")
        mainlabel.border_title = "Change this label"
        yield mainlabel
        countinglabel = Label("Press a button", id="countinglabel")
        countinglabel.border_title = "Button counter"
        yield countinglabel
      
    @on(Button.Pressed)
    def change_label_style(self, event):
        self.BUTTON_PRESSES += 1
        mainlabel = self.query_one("#mainlabel")
        if event.button.id == "colorbutton":
            mainlabel.styles.color = next(COLORS)
            mainlabel.styles.border_title_color = next(COLORS)
            mainlabel.styles.border = ("double", next(COLORS))
            
        elif event.button.id == "layoutbutton":
            mainlabel.styles.dock = next(DOCKS)
        countinglabel = self.query_one("#countinglabel")
        countinglabel.update(f"There have been {self.BUTTON_PRESSES} button presses")
     
    @on(Input.Changed)
    def change_label_text(self, event):
        mainlabel = self.query_one("#mainlabel")
        mainlabel.update(event.value)





if __name__ == "__main__":
    app = LabelsAndButtonsApp()
    app.run()
