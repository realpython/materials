def total(prices):
    t = 0
    for p in prices:
        t = t + p
    return t


def average(prices):
    return total(prices) / len(prices)
