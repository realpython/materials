from textual.app import App
from textual.containers import Vertical
from textual.widgets import Static

NUM_BOXES = 4


class VerticalLayoutAppWithTCSS(App):
    CSS_PATH = "vertical_layout.tcss"

    def compose(self):
        with Vertical():
            for i in range(NUM_BOXES):
                yield Static(f"Static {i + 1}")


if __name__ == "__main__":
    app = VerticalLayoutAppWithTCSS()
    app.run()
