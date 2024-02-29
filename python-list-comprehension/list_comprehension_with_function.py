prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08


def get_price_with_tax(price):
    return price * (1 + TAX_RATE)


final_prices = [get_price_with_tax(price) for price in prices]
print(final_prices)
