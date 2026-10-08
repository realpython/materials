class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    # 'Order' is deliberately unresolvable here: the runtime import is
    # gone but the annotation still names it. step2 guards the import.
    def is_in_order(self, order: Order) -> bool:  # noqa: F821
        return order.product.name == self.name
