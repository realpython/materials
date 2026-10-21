class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __bool__(self):
        return len(self.cart) > 0
