from typing import TYPE_CHECKING, get_type_hints

if TYPE_CHECKING:
    from decimal import Decimal

def to_pennies(amount: Decimal) -> int:
    return int(amount * 100)

print(get_type_hints(to_pennies))
