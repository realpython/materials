from datetime import UTC, datetime

from orders.domain.models import Order
from orders.domain.pricing import discounted_total
from orders.services.ports import OrderRepository


def place_order(order: Order, repo: OrderRepository) -> str:
    """Save the order and return a receipt line."""
    repo.save(order)
    placed_at = datetime.now(UTC).isoformat(timespec="seconds")
    return f"{order.order_id}: {discounted_total(order)} at {placed_at}"
