"""Collapse duplicate CSV rows by putting them in a set of frozendicts.

Each row that csv.DictReader yields is a dict, which is unhashable and so can't
go in a set. Freezing each row makes the whole deduplication one expression.

Watch the orders 1002 and 1003: they survive as two entries each, because their
fetched_at timestamps differ. That's a lesson about picking the fields that
define identity, not a bug.

Run with Python 3.15 or later:

    python dedupe_csv.py
"""

import csv
import io
from operator import itemgetter

ORDERS = """\
order_id,customer,amount,fetched_at
1001,Ada,250.00,2026-08-13T09:00:00
1002,Grace,80.50,2026-08-13T09:00:00
1001,Ada,250.00,2026-08-13T09:00:00
1003,Linus,42.00,2026-08-13T09:00:00
1002,Grace,80.50,2026-08-13T09:05:00
1003,Linus,99.00,2026-08-13T09:05:00
"""


def main():
    rows = list(csv.DictReader(io.StringIO(ORDERS)))
    unique_rows = {frozendict(row) for row in rows}

    print(
        f"Read {len(rows)} rows, kept {len(unique_rows)} after deduplication."
    )
    for row in sorted(unique_rows, key=itemgetter("order_id", "fetched_at")):
        print(f"  {row['order_id']} {row['customer']:<6} {row['fetched_at']}")

    identity = itemgetter("order_id", "customer", "amount")
    by_order = {
        frozendict(zip(("order_id", "customer", "amount"), identity(row)))
        for row in rows
    }
    print(f"Ignoring fetched_at leaves {len(by_order)} orders.")


if __name__ == "__main__":
    main()
