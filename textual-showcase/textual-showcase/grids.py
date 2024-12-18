from textual.app import App
from textual.containers import Container
from textual.widgets import Static


class Grids(App):
    CSS_PATH = "grids.tcss"

    def compose(self):
        with Container(id="maingrid"):
            yield Static("Top Left")
            yield Static("Right", id="right")
            with Container(id="subgrid"):
                yield Static("Bottom Left.1", id="bottomleft1")
                yield Static("Bottom Left.2")
                yield Static("Bottom Left.3")
                yield Static("Bottom Left.4", id="bottomleft4")


if __name__ == "__main__":
    app = Grids()
    app.run()
