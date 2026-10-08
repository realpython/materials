# Avoid this:
# TAX_RATE = 0.20

# def calculate_tax(amount):
#     """Return the tax for the given amount."""
#     return round_amount(amount * TAX_RATE)

# def round_amount(amount, decimals=2):
#     return round(amount, decimals)


# Favor this:
__all__ = ["TAX_RATE", "calculate_tax"]  # Optional

TAX_RATE = 0.20


def calculate_tax(amount):
    """Return the tax for the given amount."""
    return _round_amount(amount * TAX_RATE)


def _round_amount(amount: float, decimals=2):
    return round(amount, decimals)
