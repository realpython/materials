from textual.app import App
from textual.containers import Vertical
from textual.widgets import Static

NUM_BOXES = 4


class VerticalLayoutApp(App):
    def compose(self):
        with Vertical():
            for i in range(NUM_BOXES):
                static = Static(f"Static {i + 1}")
                static.styles.border = ("solid", "green")
                yield static

        # for i in range(NUM_BOXES):
        #     static = Static(f"Static {i + 1}")
        #     static.styles.border = ("solid", "green")
        #     yield static


if __name__ == "__main__":
    app = VerticalLayoutApp()
    app.run()
