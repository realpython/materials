from textual.app import App, ComposeResult
from textual.widgets import Static, Label


class StaticAndLabelApp(App):

    def compose(self) -> ComposeResult:
        self.static = Static("I am a [bold red]Static[/bold red] widget!")
        yield self.static
        self.label =Label("I am a [yellow italic]Label[/yellow italic] widget!")
        yield self.label

    def on_mount(self) -> None:
        self.static.styles.background = "blue"
        self.static.styles.border = ("solid", "white")
        self.static.styles.text_align = "center"
        self.static.styles.padding = 1, 1
        self.static.styles.margin = 4, 4
        self.label.styles.background = "darkgreen"
        self.label.styles.border = ("double", "red")
        self.label.styles.padding = 1, 1
        self.label.styles.margin = 2, 4
   
if __name__ == "__main__":
    StaticAndLabelApp().run()
