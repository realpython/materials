from textual.app import App
from textual.containers import VerticalScroll
from textual.widgets import Static

NUM_BOXES = 20


class VerticalScrollApp(App):
    CSS_PATH = "vertical_layout.tcss"

    def compose(self):
        with VerticalScroll():
            for i in range(NUM_BOXES):
                yield Static(f"Static {i + 1}")


if __name__ == "__main__":
    app = VerticalScrollApp()
    app.run()
