import timeit

def calculate_order_total(items):
    total = 0
    for item in items:
        total = total + item["price"] * item["quantity"]
    return total

order = [
    {"price": 19.99, "quantity": 3},
    {"price": 5.50, "quantity": 10},
    {"price": 42.00, "quantity": 1},
] * 100

print(calculate_order_total(order))

order_time = timeit.timeit(
    lambda: calculate_order_total(order), number=500_000
)
print(f"calculate_order_total: {order_time:.4f} seconds")