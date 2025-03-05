# def calcTotal(price,taxRate=0.05): return price*(1+taxRate)


def calculate_price_with_taxes(
    base_price: float, tax_rate: float = 0.05
) -> float:
    return base_price * (1 + tax_rate)
