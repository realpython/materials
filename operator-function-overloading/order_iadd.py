class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __iadd__(self, other):
        self.cart.append(other)
        return self
