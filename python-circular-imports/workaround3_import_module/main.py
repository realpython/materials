from shop.product import Product

laptop = Product("Laptop", 1000.0)
order = laptop.order(1)
order.add_shipping()

print(order.get_total())
