from typing import Protocol

from orders.domain.models import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...

    def get(self, order_id: str) -> Order | None: ...
