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

runs = 500_000

print(f"{calculate_order_total(order):.2f}")

order_time = timeit.timeit(lambda: calculate_order_total(order), number=runs)
print(f"total for {runs:,} runs: {order_time:.4f} seconds")
print(f"per call: {order_time / runs * 1_000_000:.1f} microseconds")
