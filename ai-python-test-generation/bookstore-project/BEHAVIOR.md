# Bookstore Behavior

Intended behavior of the `bookstore` package, one section per public callable.
Rows are checked against the docstrings and the pricing tables. Money values
are `Decimal`, and prices in the catalog are strings.

# `bookstore/pricing.py`

## `volume_discount(quantity)`

Returns the bulk discount rate for an order of `quantity` books.

Source: docstring. Orders of 10 or more books get 5% off, and orders of 50 or
more get 12% off.

| quantity | expected                                       | note     |
| -------- | ---------------------------------------------- | -------- |
| -1       | raises ValueError: "quantity must be positive" | error    |
| 0        | raises ValueError: "quantity must be positive" | error    |
| 1        | Decimal("0.00")                                | edge     |
| 9        | Decimal("0.00")                                | boundary |
| 10       | Decimal("0.05")                                | boundary |
| 11       | Decimal("0.05")                                | boundary |
| 49       | Decimal("0.05")                                | boundary |
| 50       | Decimal("0.12")                                | boundary |
| 51       | Decimal("0.12")                                | boundary |

## `member_discount(member_tier)`

Returns the discount rate for a membership tier.

Source: `MEMBER_DISCOUNTS` table.

| member_tier | expected                                   | note  |
| ----------- | ------------------------------------------ | ----- |
| "none"      | Decimal("0.00")                            | happy |
| "plus"      | Decimal("0.05")                            | happy |
| "pro"       | Decimal("0.10")                            | happy |
| "gold"      | raises ValueError: "unknown tier: gold"    | error |
| ""          | raises ValueError: "unknown tier: "        | edge  |

## `tax_rate(country)`

Returns the sales tax rate for a country code.

Source: `TAX_RATES` table.

| country | expected                                    | note  |
| ------- | ------------------------------------------- | ----- |
| "US"    | Decimal("0.00")                             | happy |
| "GB"    | Decimal("0.20")                             | happy |
| "DE"    | Decimal("0.19")                             | happy |
| "FR"    | raises ValueError: "unknown country: FR"    | error |

## `shipping_cost(subtotal)`

Returns the shipping charge for a discounted subtotal.

Source: docstring, `FREE_SHIPPING_THRESHOLD`, and `SHIPPING_FEE`. Orders of
$35.00 or more ship free. Smaller orders pay $4.99.

| subtotal         | expected        | note     |
| ---------------- | --------------- | -------- |
| Decimal("0.00")  | Decimal("4.99") | edge     |
| Decimal("34.99") | Decimal("4.99") | boundary |
| Decimal("35.00") | Decimal("0.00") | boundary |
| Decimal("35.01") | Decimal("0.00") | boundary |

## `quote_order(quantity, unit_price, member_tier="none", country="US")`

Prices an order and returns the total the customer pays.

Source: docstring and the callables above. The order of operations is:

1. Multiply `unit_price` by `quantity`.
2. Apply the volume discount, then the member discount.
3. Round the discounted subtotal to cents, half up.
4. Add shipping, based on the discounted subtotal.
5. Add tax on the subtotal plus shipping, rounded to cents, half up.

| quantity | unit_price | member_tier | country | expected                                              | note                                     |
| -------- | ---------- | ----------- | ------- | ----------------------------------------------------- | ---------------------------------------- |
| 1        | "39.99"    | "none"      | "US"    | Decimal("39.99")                                      | happy, ships free                        |
| 1        | "20.00"    | "none"      | "US"    | Decimal("24.99")                                      | adds shipping                            |
| 1        | "34.99"    | "none"      | "US"    | Decimal("39.98")                                      | boundary, pays shipping                  |
| 1        | "35.00"    | "none"      | "US"    | Decimal("35.00")                                      | boundary, ships free                     |
| 1        | "0.00"     | "none"      | "US"    | Decimal("4.99")                                       | edge, free book still pays shipping      |
| 10       | "39.99"    | "none"      | "US"    | Decimal("379.91")                                     | volume discount, 379.905 rounds half up  |
| 2        | "20.00"    | "pro"       | "US"    | Decimal("36.00")                                      | member discount, ships free              |
| 2        | "18.00"    | "plus"      | "US"    | Decimal("39.19")                                      | discount drops subtotal below free ship  |
| 1        | "20.00"    | "none"      | "GB"    | Decimal("29.99")                                      | tax applies to shipping too              |
| 1        | "39.99"    | "none"      | "DE"    | Decimal("47.59")                                      | tax rounds half up                       |
| 50       | "10.00"    | "pro"       | "GB"    | Decimal("475.20")                                     | every discount and tax combined          |
| 0        | "10.00"    | "none"      | "US"    | raises ValueError: "quantity must be positive"        | error                                    |
| 1        | "-0.01"    | "none"      | "US"    | raises ValueError: "unit price must not be negative"  | error                                    |
| 1        | "10.00"    | "gold"      | "US"    | raises ValueError: "unknown tier: gold"               | error                                    |
| 1        | "10.00"    | "none"      | "FR"    | raises ValueError: "unknown country: FR"              | error                                    |

When `member_tier` and `country` are omitted, the order is priced as a
non-member in the US: `quote_order(1, "20.00")` returns `Decimal("24.99")`.

# `bookstore/catalog.py`

## `Catalog(path=None)`

Read-only access to book records in a JSON file. Each record has `isbn`,
`title`, `author`, and `price` keys.

Source: class and method docstrings, and `bookstore/data/books.json`.

| given                                  | action                   | expected                                                 | note  |
| -------------------------------------- | ------------------------ | -------------------------------------------------------- | ----- |
| no path                                | `.books` keys            | the four ISBNs in `bookstore/data/books.json`, in order  | happy |
| path to a missing file                 | construct                | no error, since the file isn't read yet                  | edge  |
| path to a missing file                 | `.books`                 | raises FileNotFoundError                                 | error |
| file with two records                  | `.books`                 | dict of both records keyed by ISBN                       | happy |
| file with `[]`                         | `.books`                 | `{}`                                                     | edge  |
| `.books` already read, file rewritten  | `.books`                 | the original records, since the file is read once        | edge  |
| `.books` already read, file rewritten  | `.load()` then `.books`  | the new records                                          | happy |
| any file                               | `.load()`                | returns the same `Catalog` instance                      | happy |

## `Catalog.get(isbn)`

| given                   | isbn        | expected                                   | note  |
| ----------------------- | ----------- | ------------------------------------------ | ----- |
| file with two records   | stocked     | that record's dict                         | happy |
| file with two records   | "000"       | raises KeyError: "unknown isbn: 000"       | error |

## `Catalog.price_of(isbn)`

| given                                  | isbn     | expected                               | note  |
| -------------------------------------- | -------- | -------------------------------------- | ----- |
| record with price "39.99"              | stocked  | "39.99"                                | happy |
| file with two records                  | "000"    | raises KeyError: "unknown isbn: 000"   | error |

## `Catalog.by_author(author)`

| given                                      | author          | expected                           | note  |
| ------------------------------------------ | --------------- | ---------------------------------- | ----- |
| two books by "Dan Bader", one by another   | "Dan Bader"     | both records, in catalog order     | happy |
| no books by the author                     | "Nobody"        | `[]`                               | edge  |

# `bookstore/inventory.py`

## `Inventory(stock=None)`

Tracks on-hand and reserved copies per ISBN. `on_hand` counts copies in the
warehouse, `reserved` counts copies held for unshipped orders, and
`available` is `on_hand - reserved`.

Source: class and method docstrings.

| given                                    | action                  | expected                                  | note  |
| ---------------------------------------- | ----------------------- | ----------------------------------------- | ----- |
| `{"A": 5}`                               | `on_hand("A")`          | 5                                         | happy |
| `{"A": 5}`                               | `on_hand("B")`          | 0                                         | edge  |
| `{"A": 5}`                               | `reserved("A")`         | 0                                         | edge  |
| `{"A": 5}`                               | `available("A")`        | 5                                         | happy |
| no stock                                 | `on_hand("A")`          | 0                                         | edge  |
| `{"A": 5}`, caller then edits their dict | `on_hand("A")`          | 5, since the inventory keeps its own copy | edge  |

## `Inventory.reserve(isbn, quantity)`

Holds copies and returns what's left available.

| given                    | isbn | quantity | expected                                                  | note     |
| ------------------------ | ---- | -------- | --------------------------------------------------------- | -------- |
| `{"A": 5}`               | "A"  | 2        | returns 3, `reserved("A")` is 2, `on_hand("A")` is 5      | happy    |
| `{"A": 5}`, 2 reserved   | "A"  | 1        | returns 2, `reserved("A")` is 3                           | happy    |
| `{"A": 5}`               | "A"  | 5        | returns 0                                                 | boundary |
| `{"A": 5}`               | "A"  | 6        | raises ValueError: "only 5 copies of A available"         | boundary |
| `{"A": 5}`, 2 reserved   | "A"  | 4        | raises ValueError: "only 3 copies of A available"         | boundary |
| `{"A": 5}`               | "A"  | 0        | raises ValueError: "quantity must be positive"            | error    |
| `{"A": 5}`               | "B"  | 1        | raises KeyError: "unknown isbn: B"                        | error    |

## `Inventory.release(isbn, quantity)`

Returns held copies to the pool and returns what's available.

| given                    | isbn | quantity | expected                                                  | note     |
| ------------------------ | ---- | -------- | --------------------------------------------------------- | -------- |
| `{"A": 5}`, 3 reserved   | "A"  | 1        | returns 3, `reserved("A")` is 2                           | happy    |
| `{"A": 5}`, 3 reserved   | "A"  | 3        | returns 5, `reserved("A")` is 0                           | boundary |
| `{"A": 5}`, 3 reserved   | "A"  | 4        | raises ValueError: "cannot release 4, only 3 reserved"    | boundary |
| `{"A": 5}`               | "A"  | 0        | raises ValueError: "quantity must be positive"            | error    |
| `{"A": 5}`               | "B"  | 1        | raises KeyError: "unknown isbn: B"                        | error    |

## `Inventory.commit(isbn, quantity)`

Ships held copies, removing them from stock, and returns what's on hand.

| given                    | isbn | quantity | expected                                                                    | note     |
| ------------------------ | ---- | -------- | --------------------------------------------------------------------------- | -------- |
| `{"A": 5}`, 3 reserved   | "A"  | 2        | returns 3, `reserved("A")` is 1, `available("A")` is 2                      | happy    |
| `{"A": 5}`, 3 reserved   | "A"  | 3        | returns 2, `reserved("A")` is 0                                             | boundary |
| `{"A": 5}`, 3 reserved   | "A"  | 4        | raises ValueError: "cannot ship 4, only 3 reserved"                         | boundary |
| `{"A": 5}`               | "A"  | 0        | raises ValueError: "quantity must be positive"                              | error    |
| `{"A": 5}`               | "B"  | 1        | raises KeyError: "unknown isbn: B"                                          | error    |
