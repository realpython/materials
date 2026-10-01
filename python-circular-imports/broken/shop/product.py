from shop.order import Order


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def order(self, quantity: int) -> Order:
        return Order(self, quantity)

    def is_in_order(self, order: Order) -> bool:
        return order.product.name == self.name
