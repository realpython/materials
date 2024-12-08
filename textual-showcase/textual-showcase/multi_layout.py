from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import (Markdown, OptionList, RadioSet, Select,
    SelectionList, Static, Header, Label, Digits)

from jabberwocky import JABBERWOCKY, WORDS, PI

class MultiLayoutApp(App):
    CSS_PATH = "multi_layout.tcss"
    def compose(self) -> ComposeResult:
        with Container(id="app-grid"):
            with VerticalScroll(id="top-left"):
                yield Label("...", id="docking-label")
                yield Markdown(JABBERWOCKY * 10)
            with Horizontal(id="top-right"):
                yield OptionList(*WORDS, tooltip="OptionList")
                yield Select(
                    [(word, index+1) for index, word in enumerate(WORDS)]
                    ,tooltip="Select"
                )
                yield RadioSet(*WORDS, tooltip="RadioSet")
                yield SelectionList(
                    *[(word, index+1) for index, word in enumerate(WORDS)]
                )
            with Container(id="smallgrid"):
                yield Static("Rows 1 & 2 Col 1", id="smallgrid-left")
                yield Static("Row 1 Col 2")
                yield Static("Row 1 Col 3")
                yield Static("Row 2 Cols 2 & 3", id="smallgrid-bottom-right")
            with Container (id="bottom-right"):
                yield Digits(PI)          
    
    def on_mount(self) -> None:
        self.query_one("#docking-label").border_title = "Jabberwocky"
        self.query_one("#docking-label").border_subtitle = "by Lewis Carroll"
        self.query_one(Horizontal).border_subtitle = "Select some words"
        self.query_one("#bottom-left").border_subtitle = "Grid layout"

        
if __name__ == "__main__":
    app = MultiLayoutApp()
    app.run()
