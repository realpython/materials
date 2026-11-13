def compute_total(prices):
    total = 0
    for price in prices:
        total = total + price
    return total


def compute_average(prices):
    return compute_total(prices) / len(prices)
