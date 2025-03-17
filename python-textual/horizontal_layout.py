from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Static

NUM_BOXES = 4


class HorizontalLayoutApp(App):
    def compose(self):
        with Horizontal():
            for i in range(NUM_BOXES):
                static = Static(f"Static {i + 1}")
                static.styles.border = ("solid", "green")
                static.styles.width = "10%"
                yield static


if __name__ == "__main__":
    app = HorizontalLayoutApp()
    app.run()
