from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OrderLine:
    sku: str
    quantity: int
    unit_price: Decimal

    @property
    def total(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass(frozen=True)
class Order:
    order_id: str
    lines: tuple[OrderLine, ...]

    @property
    def total(self) -> Decimal:
        return sum((line.total for line in self.lines), Decimal(0))
