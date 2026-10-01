from typing import TYPE_CHECKING

from shop import product

if TYPE_CHECKING:
    from shop.product import Product

SHIPPING_FEE = 4.99

DEFAULT_PRODUCT = product.Product("product_a", 0.0)


class Order:
    def __init__(self, product: "Product", quantity: int) -> None:
        self.product = product
        self.quantity = quantity
        self.extras: list["Product"] = []

    def add_shipping(self) -> None:
        self.extras.append(product.Product("Shipping", SHIPPING_FEE))

    def get_total(self) -> float:
        subtotal = self.product.price * self.quantity
        return subtotal + sum(extra.price for extra in self.extras)
