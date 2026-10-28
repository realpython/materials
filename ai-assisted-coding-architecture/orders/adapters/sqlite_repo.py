import json
import sqlite3
from decimal import Decimal

from orders.domain.models import Order, OrderLine


class SqliteOrderRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self._db = connection
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS orders "
            "(id TEXT PRIMARY KEY, body TEXT)"
        )

    def save(self, order: Order) -> None:
        body = json.dumps(
            [[ln.sku, ln.quantity, str(ln.unit_price)] for ln in order.lines]
        )
        self._db.execute(
            "INSERT OR REPLACE INTO orders VALUES (?, ?)",
            (order.order_id, body),
        )

    def get(self, order_id: str) -> Order | None:
        row = self._db.execute(
            "SELECT body FROM orders WHERE id = ?", (order_id,)
        ).fetchone()
        if row is None:
            return None
        lines = tuple(
            OrderLine(sku, qty, Decimal(price))
            for sku, qty, price in json.loads(row[0])
        )
        return Order(order_id, lines)
