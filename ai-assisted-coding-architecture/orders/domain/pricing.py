from decimal import Decimal

from orders.domain.models import Order

BULK_THRESHOLD = Decimal(100)
BULK_DISCOUNT = Decimal("0.10")


def discounted_total(order: Order) -> Decimal:
    if order.total >= BULK_THRESHOLD:
        return order.total * (1 - BULK_DISCOUNT)
    return order.total
