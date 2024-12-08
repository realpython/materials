# from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (
    Header,
    Label,
    SelectionList,
    Sparkline,
    TabbedContent,
    Tree,
    Placeholder,
)


class TabbedLayoutApp(App):
    CSS = """
    Placeholder {
        color: yellow;
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent("Options", "Tree", "Sparklines"):
            yield Placeholder("Here I am!")
            yield Placeholder("Placeholder 2")
            yield Placeholder("Placeholder 3")


if __name__ == "__main__":
    TabbedLayoutApp().run()
