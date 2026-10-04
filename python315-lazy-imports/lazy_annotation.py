import sys
from typing import get_type_hints

lazy from decimal import Decimal

def to_pennies(amount: Decimal) -> int:
    return int(amount * 100)

print("decimal loaded?", "decimal" in sys.modules)
print(get_type_hints(to_pennies))
print("decimal loaded?", "decimal" in sys.modules)
