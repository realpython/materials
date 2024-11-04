from textual.app import App, ComposeResult
from textual.widgets import Static


class HelloTextualApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Hello, Textual!")


if __name__ == "__main__":
    HelloTextualApp().run()
