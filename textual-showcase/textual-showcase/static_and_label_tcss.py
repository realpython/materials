from textual.app import App, ComposeResult
from textual.widgets import Static, Label


class StaticAndLabelAppWithTCSS(App):
    CSS_PATH = "static_and_label.tcss"

    def compose(self) -> ComposeResult:
        yield Static("I am a [bold red]Static[/bold red] widget!")
        yield Label("I am a [yellow italic]Label[/yellow italic] widget!")


if __name__ == "__main__":
    StaticAndLabelAppWithTCSS().run()
