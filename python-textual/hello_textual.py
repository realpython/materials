from textual.app import App
from textual.widgets import Static


class HelloTextualApp(App):
    def compose(self):
        yield Static("Hello, Textual!")


if __name__ == "__main__":
    app = HelloTextualApp()
    app.run()
