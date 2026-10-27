"""Order pricing."""

from decimal import ROUND_HALF_UP, Decimal

FREE_SHIPPING_THRESHOLD = Decimal("35.00")
SHIPPING_FEE = Decimal("4.99")

MEMBER_DISCOUNTS = {
    "none": Decimal("0.00"),
    "plus": Decimal("0.05"),
    "pro": Decimal("0.10"),
}

TAX_RATES = {
    "US": Decimal("0.00"),
    "GB": Decimal("0.20"),
    "DE": Decimal("0.19"),
}


def _money(amount):
    """Round to cents, half up."""
    return Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def volume_discount(quantity):
    """Return the bulk discount rate for an order of this size.

    Orders of 10 or more books get 5% off, and orders of 50 or more
    get 12% off. Smaller orders get no discount.
    """
    if quantity < 1:
        raise ValueError("quantity must be positive")
    if quantity >= 50:
        return Decimal("0.12")
    if quantity >= 10:
        return Decimal("0.05")
    return Decimal("0.00")


def member_discount(member_tier):
    """Return the discount rate for a membership tier."""
    try:
        return MEMBER_DISCOUNTS[member_tier]
    except KeyError:
        raise ValueError(f"unknown tier: {member_tier}") from None


def tax_rate(country):
    """Return the sales tax rate for a country."""
    try:
        return TAX_RATES[country]
    except KeyError:
        raise ValueError(f"unknown country: {country}") from None


def shipping_cost(subtotal):
    """Return the shipping charge for a discounted subtotal."""
    if subtotal >= FREE_SHIPPING_THRESHOLD:
        return Decimal("0.00")
    return SHIPPING_FEE


def quote_order(quantity, unit_price, member_tier="none", country="US"):
    """Price an order and return the total the customer pays."""
    if quantity < 1:
        raise ValueError("quantity must be positive")

    unit_price = Decimal(str(unit_price))
    if unit_price < 0:
        raise ValueError("unit price must not be negative")

    subtotal = unit_price * quantity
    subtotal *= Decimal("1") - volume_discount(quantity)
    subtotal *= Decimal("1") - member_discount(member_tier)
    subtotal = _money(subtotal)

    shipping = shipping_cost(subtotal)
    taxable = subtotal + shipping
    return _money(taxable + _money(taxable * tax_rate(country)))
