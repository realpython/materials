
# from textual import on
from textual.app import App
from textual.widgets import Button, Digits, Footer

class EventsApp(App):
    CSS_PATH = "events.tcss"
    BINDINGS = [("q", "quit", "Quit"), ("b", "toggle_border", "Toggle border")] 

    presses_count = 0
    double_border = False
    def compose(self):
        yield Button(
            "Click me!",
            id="button",
        )
        self.digits = Digits("0", id="digits")
        self.digits.border_subtitle = "Button presses"
        yield self.digits
        yield Footer()

    def on_button_pressed(self, event):
        self.presses_count += 1
        if event.button.id == "button":
            self.digits.update(f"{self.presses_count}")

    # Alternatively
    # @on(Button.Pressed, "#button")
    # def change_digit(self, event):
    #     self.presses_count += 1
    #     digits = self.query_one("#digits")
    #     digits.update(f"{self.presses_count}")

    def action_toggle_border(self):
        self.double_border = not self.double_border
        if self.double_border:
            self.digits.styles.border = ("double", "yellow")
        else:
            self.digits.styles.border = ("solid", "white")
 
if __name__ == "__main__":
    app = EventsApp()
    app.run()