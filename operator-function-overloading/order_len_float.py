class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return float(len(self.cart))  # Return type changed to float
