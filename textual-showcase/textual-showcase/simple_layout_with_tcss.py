from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class SimpleLayoutApp(App):
    CSS_PATH = "simple_layout.tcss"
    def compose(self) -> ComposeResult:
        with Vertical():
            self.widget1 = Static("   :point_up:\nCentered", id="widget1")
            yield self.widget1
            with Horizontal():
                self.widget2 = Static(":point_left: Left Aligned", id="widget2")
                yield self.widget2
                self.widget3 = Static("Right Aligned :point_right:", id="widget3")
                yield self.widget3

    

if __name__ == "__main__":
    app = SimpleLayoutApp()
    app.run()
