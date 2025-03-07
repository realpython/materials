from textual.app import App
from textual.containers import Grid
from textual.widgets import Static


class GridLayoutApp(App):
    def compose(self):
        grid = Grid()
        grid.styles.grid_size_rows = rows = 6
        grid.styles.grid_size_columns = cols = 4
        with grid:
            for row in range(rows):
                for col in range(cols):
                    static = Static(f"Static ({row=}, {col=})")
                    static.styles.border = ("solid", "green")
                    static.styles.width = "1fr"
                    static.styles.height = "1fr"
                    yield static


if __name__ == "__main__":
    app = GridLayoutApp()
    app.run()
