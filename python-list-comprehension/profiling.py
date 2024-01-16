import random
import timeit

TAX_RATE = 0.08
PRICES = [random.randrange(100) for _ in range(100_000)]


def get_price(price):
    return price * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, PRICES))


def get_prices_with_comprehension():
    return [get_price(price) for price in PRICES]


def get_prices_with_loop():
    prices = []
    for price in PRICES:
        prices.append(get_price(price))
    return prices


print(timeit.timeit(get_prices_with_map, number=100))
print(timeit.timeit(get_prices_with_comprehension, number=100))
print(timeit.timeit(get_prices_with_loop, number=100))
