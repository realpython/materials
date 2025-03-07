# from textual import on
from textual.app import App
from textual.widgets import Button, Digits, Footer


class EventsApp(App):
    CSS_PATH = "events.tcss"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("b", "toggle_border", "Toggle border"),
    ]

    presses_count = 0
    double_border = False

    def compose(self):
        yield Button("Click me!", id="button")
        digits = Digits("0", id="digits")
        digits.border_subtitle = "Button presses"
        yield digits
        yield Footer()

    def action_toggle_border(self):
        self.double_border = not self.double_border
        digits = self.query_one("#digits")
        if self.double_border:
            digits.styles.border = ("double", "yellow")
        else:
            digits.styles.border = ("solid", "white")

    def on_button_pressed(self, event):
        if event.button.id == "button":
            self.presses_count += 1
            digits = self.query_one("#digits")
            digits.update(f"{self.presses_count}")

    # @on(Button.Pressed, "#button")
    # def button_pressed(self, event):
    #     self.presses_count += 1
    #     digits = self.query_one("#digits")
    #     digits.update(f"{self.presses_count}")


if __name__ == "__main__":
    app = EventsApp()
    app.run()
