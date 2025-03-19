from textual.app import App
from textual.containers import Grid
from textual.widgets import Static


class GridLayoutAppWithTCSS(App):
    CSS_PATH = "grid.tcss"

    def compose(self):
        with Grid():
            for row in range(6):
                for col in range(4):
                    yield Static(f"Static ({row=}, {col=})")


if __name__ == "__main__":
    app = GridLayoutAppWithTCSS()
    app.run()
