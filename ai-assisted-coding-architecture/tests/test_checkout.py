import sqlite3
from decimal import Decimal

from orders.adapters.sqlite_repo import SqliteOrderRepository
from orders.domain.models import Order, OrderLine
from orders.services.checkout import place_order


def test_place_order_round_trip():
    repo = SqliteOrderRepository(sqlite3.connect(":memory:"))
    order = Order("A1", (OrderLine("pen", 20, Decimal("6.00")),))
    receipt = place_order(order, repo)
    assert receipt.startswith("A1: 108.0000 at ")
    assert repo.get("A1") == order
