fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}


def has_low_price(item, price=0.4):
    return item[1] < price


dict(filter(has_low_price, fruits.items()))
