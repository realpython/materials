from textual.app import App
from textual.containers import Horizontal, HorizontalScroll, VerticalScroll
from textual.widgets import Label, Static

NUM_BOXES = 12


class NestedContainersApp(App):
    CSS_PATH = "layouts.tcss"

    def compose(self):
        with Horizontal(id="horizontal"):
            yield Static("Left", classes="box")
            with HorizontalScroll(id="horizontalscroll"):
                for i in range(NUM_BOXES):
                    yield Static(
                        f"Center.{i + 1}",
                        classes="box yellowbox",
                    )
            with VerticalScroll(id="verticalscroll"):
                for i in range(NUM_BOXES):
                    yield Static(
                        f"Right.{i + 1}",
                        classes="box redbox",
                    )
                yield Label(
                    "I am a docked label.\nI don't move!",
                    id="docked-label",
                )


if __name__ == "__main__":
    app = NestedContainersApp()
    app.run()
