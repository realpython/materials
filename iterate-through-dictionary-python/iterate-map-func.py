fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}


def apply_discount(product, discount=0.05):
    return product[0], round(product[1] * (1 - discount), 2)


dict(map(apply_discount, fruits.items()))
dict(map(lambda item: apply_discount(item, 0.1), fruits.items()))
dict(map(lambda item: apply_discount(item, 0.15), fruits.items()))
