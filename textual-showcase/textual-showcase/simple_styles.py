from textual.app import App, ComposeResult
from textual.widgets import Button, Label, ListView, ListItem, Header, Footer


class SimpleStylesApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        self.styled_button = Button("Moons of Jupiter")
        yield self.styled_button
        self.styled_list = ListView(
            ListItem(Label("Ganymede")),
            ListItem(Label("Callisto")),
            ListItem(Label("Io")),
            ListItem(Label("Europa")),
        )
        yield self.styled_list

    def on_mount(self) -> None:
        self.screen.styles.border = ("panel", "gray")
        self.screen.styles.align = ("center", "middle")

        self.styled_button.styles.padding = 1
        self.styled_button.styles.margin = 2
        self.styled_button.styles.background = "darkgreen"
        self.styled_button.styles.color = "black"

        self.styled_list.styles.background = "gray"
        self.styled_list.styles.border = ("double", "yellow")
        self.styled_list.styles.width = 12
        self.styled_list.styles.height = "auto"


if __name__ == "__main__":
    app = SimpleStylesApp()
    app.run()
