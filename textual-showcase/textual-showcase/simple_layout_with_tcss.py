from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class SimpleLayoutWithTCSSApp(App):
    CSS_PATH = "simple_layout.tcss"

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("   :point_up:\nCentered", id="widget1")
            with Horizontal():
                yield Static(":point_left: Left Aligned", id="widget2")
                yield Static("Right Aligned :point_right:", id="widget3")


if __name__ == "__main__":
    app = SimpleLayoutWithTCSSApp()
    app.run()
