from textual.app import App
from textual.containers import HorizontalScroll
from textual.widgets import Static

NUM_BOXES = 20


class HorizontalScrollApp(App):
    def compose(self):
        with HorizontalScroll():
            for i in range(NUM_BOXES):
                static = Static(f"Static {i + 1}")
                static.styles.border = ("solid", "green")
                static.styles.width = "10%"
                yield static


if __name__ == "__main__":
    app = HorizontalScrollApp()
    app.run()
