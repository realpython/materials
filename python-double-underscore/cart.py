class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products

    def __len__(self):
        return len(self.products)

    # Implementation...
