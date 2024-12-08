from textual.app import App, ComposeResult
from textual.widgets import Placeholder


class MyApp(App):
    CSS_PATH = "test.tcss"

    def compose(self) -> ComposeResult:
        yield Placeholder("A", id="A")
        yield Placeholder("B", id="B")
        yield Placeholder("C", id="C")


if __name__ == "__main__":
    MyApp().run()
