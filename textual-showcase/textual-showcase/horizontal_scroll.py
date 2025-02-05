from textual.app import App
from textual.containers import HorizontalScroll
from textual.widgets import Static

NUM_BOXES = 20
class HorizontalScrollExample(App):
 
    CSS_PATH = 'horizontal_layout.tcss'
    def compose(self):
        with HorizontalScroll():
            for i in range(NUM_BOXES):
                yield Static(f"Static {i+1}")
 
if __name__ == "__main__":
    app = HorizontalScrollExample()
    app.run()