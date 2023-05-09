from typing import NamedTuple


class Item(NamedTuple):
    name: str
    price: float
    quantity: int = 1


class ShoppingCart:
    def __init__(self):
        self._cart = []
        self._total = 0.0

    def add_item(self, item):
        self._cart.append(item)
        self._total += item.price * item.quantity

    def remove_item(self, item):
        for cart_item in self._cart:
            if cart_item.name == item.name:
                self._total -= cart_item.price * cart_item.quantity
                self._cart.remove(cart_item)
                break

    def content(self):
        print("Items in cart:")
        for item in self._cart:
            print(
                f"- {item.name}: {item.quantity} x ${item.price:.2f}"
                f" = ${item.quantity * item.price:.2f}"
            )
        print(f"\nTotal: ${self._total:.2f}")

    def __call__(self):
        print("Resetting the cart...")
        self._cart = []
        self._total = 0.0
