from textual.app import App
from textual.containers import Vertical
from textual.widgets import Static

NUM_BOXES = 20
class VerticalLayoutExample(App):
 
    def compose(self):
        with Vertical():
            for i in range(NUM_BOXES):
                static = Static(f"Static {i+1}")
                static.styles.border = ("solid", "green")
                yield static

        # Vertical is the default, so we don't need to specify it.
        # for i in range(NUM_BOXES):
        #     static = Static(f"Static {i+1}")
        #     static.styles.border = ("solid", "green")
        #     yield static

if __name__ == "__main__":
    app = VerticalLayoutExample()
    app.run()