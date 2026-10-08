from shop.order import Order
from shop.product import Product

laptop = Product("Laptop", 1000.0)
order = Order(laptop, 2)
order.add_shipping()

print(order.get_total())
