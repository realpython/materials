from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Digits, Header
from textual.containers import Horizontal, HorizontalGroup


class MenuItem(HorizontalGroup):
    def __init__(self, id: str, text: str, unit_price: float) -> None:
        super().__init__(id=id)
        self.text = text
        self.quantity = 0
        self.total = 0
        self.unit_price = unit_price

    def compose(self) -> ComposeResult:
        yield Label(self.text, classes="item_label")
        yield Label(f"${self.unit_price:.2f}")
        yield Button(":heavy_plus_sign:", classes="plus")
        yield Button(":heavy_minus_sign:", classes="minus")
        yield Label("0", classes="quantity")
        yield Label("$0.00", classes="total")

    def update_display(self) -> None:
        self.total = self.quantity * self.unit_price
        self.query_one(".quantity", Label).update(f"{self.quantity}")
        self.query_one(".total", Label).update(f"${ self.total:.2f}")

    @on(Button.Pressed, ".plus")
    def add_one(self):
        self.quantity += 1
        self.update_display()

    @on(Button.Pressed, ".minus")
    def subtract_one(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.update_display()


class CalcMenuApp(App):
    CSS_PATH = "calcmenu.tcss"
    ITEMS = [
        ["pizza", ":pizza: Pizza", 12.95],
        ["hamburger", ":hamburger: Hamburger", 10.50],
        ["beer", ":beer: Beer", 4.50],
        ["wine", ":wine_glass: Wine", 6.25],
        ["cocktail", ":tropical_drink: Cocktail", 8.50],
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        for item in self.ITEMS:
            yield MenuItem(*item)
        yield Digits(f"${0: .2f}", id="grand_total")

    def on_mount(self) -> None:
        self.screen.title = "Textual's Greasy Spoon"

    @on(Button.Pressed)
    def update_grand_total(self):
        grand_total = 0
        for item in self.ITEMS:
            grand_total += self.query_one(f"#{item[0]}").total
        self.query_one("#grand_total").update(f"$ {grand_total:.2f}")


if __name__ == "__main__":
    CalcMenuApp().run()
