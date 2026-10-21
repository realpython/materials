class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __radd__(self, other):
        new_cart = self.cart.copy()
        new_cart.insert(0, other)
        return Order(new_cart, self.customer)
