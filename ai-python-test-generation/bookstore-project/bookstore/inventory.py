"""Stock tracking for the warehouse."""


class Inventory:
    """Tracks on-hand and reserved copies for each ISBN."""

    def __init__(self, stock=None):
        self._on_hand = dict(stock or {})
        self._reserved = {}

    def on_hand(self, isbn):
        """Copies physically in the warehouse."""
        return self._on_hand.get(isbn, 0)

    def reserved(self, isbn):
        """Copies held for orders that have not shipped."""
        return self._reserved.get(isbn, 0)

    def available(self, isbn):
        """Copies that can still be reserved."""
        return self.on_hand(isbn) - self.reserved(isbn)

    def _check(self, isbn, quantity):
        if quantity < 1:
            raise ValueError("quantity must be positive")
        if isbn not in self._on_hand:
            raise KeyError(f"unknown isbn: {isbn}")

    def reserve(self, isbn, quantity):
        """Hold copies for an order and return what is left available."""
        self._check(isbn, quantity)
        available = self.available(isbn)
        if quantity > available:
            raise ValueError(f"only {available} copies of {isbn} available")
        self._reserved[isbn] = self.reserved(isbn) + quantity
        return self.available(isbn)

    def release(self, isbn, quantity):
        """Return held copies to the pool and report what is available."""
        self._check(isbn, quantity)
        held = self.reserved(isbn)
        if quantity > held:
            raise ValueError(
                f"cannot release {quantity}, only {held} reserved"
            )
        self._reserved[isbn] = held - quantity
        return self.available(isbn)

    def commit(self, isbn, quantity):
        """Ship held copies, removing them from stock entirely."""
        self._check(isbn, quantity)
        held = self.reserved(isbn)
        if quantity > held:
            raise ValueError(f"cannot ship {quantity}, only {held} reserved")
        self._reserved[isbn] = held - quantity
        self._on_hand[isbn] = self.on_hand(isbn) - quantity
        return self.on_hand(isbn)
