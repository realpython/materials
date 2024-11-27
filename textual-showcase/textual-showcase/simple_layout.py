from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Static


class SimpleLayoutApp(App):
    def compose(self) -> ComposeResult:
        self.widget1 = Static("   :point_up:\nCentered")
        yield self.widget1
        with Horizontal():
            self.widget2 = Static(":point_left: Left Aligned")
            yield self.widget2
            self.widget3 = Static("Right Aligned :point_right:")
            yield self.widget3

    def on_mount(self) -> None:
        self.screen.styles.border = ("panel", "gray")
        self.screen.styles.padding = 1

        self.widget1.styles.color = "darkorange"
        self.widget1.styles.background = "darkblue"
        self.widget1.styles.border = ("heavy", "white")
        self.widget1.styles.content_align = ("center", "middle")
        self.widget1.styles.height = "1fr"

        self.widget2.styles.color = "black"
        self.widget2.styles.background = "darkgreen"
        self.widget2.styles.border = ("double", "white")
        self.widget2.styles.content_align = ("left", "middle")
        self.widget2.styles.width = "1fr"
        self.widget2.styles.height = "1fr"

        self.widget3.styles.background = "darkred"
        self.widget3.styles.border = ("dashed", "black")
        self.widget3.styles.content_align = ("right", "middle")
        self.widget3.styles.width = "1fr"
        self.widget3.styles.height = "1fr"


if __name__ == "__main__":
    app = SimpleLayoutApp()
    app.run()
