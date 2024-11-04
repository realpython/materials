from textual import on
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button, Footer, Header, ProgressBar, RadioSet


class ProgressRadioApp(App[None]):
    CSS_PATH = "progress_bar.tcss"

    TITLE = "Progress App"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Center():
            yield ProgressBar(total=100, show_eta=False)
        with Center():
            yield RadioSet("Stop", "Slow", "Medium", "Fast")
            yield Button("Reset", id="reset")
        yield Footer()

    def on_mount(self) -> None:
        self.step = 1
        self.set_interval(0.5, self.update_progress)

    def update_progress(self) -> None:
        self.query_one(ProgressBar).advance(self.step)

    @on(Button.Pressed, "#reset")
    def on_reset(self, event: Button.Pressed) -> None:
        print("Resetting progress")
        self.query_one(ProgressBar).progress = 0

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        label = event.pressed.label._text[0]
        match label:
            case "Stop":
                self.step = 0
            case "Slow":
                self.step = 1
            case "Medium":
                self.step = 5
            case "Fast":
                self.step = 20


if __name__ == "__main__":
    ProgressRadioApp().run()
