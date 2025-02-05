from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Static

NUM_BOXES = 4
class HorizontalLayoutExampleWithTCSS(App):
 
    CSS_PATH = 'horizontal_layout.tcss'
    def compose(self):
        with Horizontal():
            for i in range(NUM_BOXES):
                yield Static(f"Static {i+1}")
 
if __name__ == "__main__":
    app = HorizontalLayoutExampleWithTCSS()
    app.run()