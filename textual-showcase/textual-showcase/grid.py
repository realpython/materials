from textual.app import App
from textual.containers import Grid
from textual.widgets import Static


class GridLayoutExample(App):
    def compose(self):
        grid = Grid()
        grid.styles.grid_size_rows = 6
        grid.styles.grid_size_columns = 4

        with grid:
            for row in range(1, 7):
                for col in range(1, 5):
                    static = Static(f"Static ({row=}, {col=})")
                    static.styles.border = ("solid", "green")
                    static.styles.width = "1fr"
                    static.styles.height = "1fr"
                    yield static


if __name__ == "__main__":
    app = GridLayoutExample()
    app.run()
