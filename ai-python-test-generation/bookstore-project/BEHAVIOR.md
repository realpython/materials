# Bookstore Behavior

Intended behavior of the `bookstore` package, one section per public
callable. Rows are checked against the docstrings and the pricing tables.
Money values are `Decimal`, and prices in the catalog are strings.

# `bookstore/pricing.py`

## `volume_discount(quantity)`

Returns the bulk discount rate: 5% for 10 or more books and 12% for 50 or
more.

Source: docstring.

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

| member_tier | expected                                | note  |
| ----------- | --------------------------------------- | ----- |
| "none"      | Decimal("0.00")                         | happy |
| "plus"      | Decimal("0.05")                         | happy |
| "pro"       | Decimal("0.10")                         | happy |
| "gold"      | raises ValueError: "unknown tier: gold" | error |
| ""          | raises ValueError: "unknown tier: "     | edge  |

## `tax_rate(country)`

Returns the sales tax rate for a country code.

Source: `TAX_RATES` table.

| country | expected                                 | note  |
| ------- | ---------------------------------------- | ----- |
| "US"    | Decimal("0.00")                          | happy |
| "GB"    | Decimal("0.20")                          | happy |
| "DE"    | Decimal("0.19")                          | happy |
| "FR"    | raises ValueError: "unknown country: FR" | error |

## `shipping_cost(subtotal)`

Returns the shipping charge for a discounted subtotal: free from $35.00,
and $4.99 below that.

Source: docstring, `FREE_SHIPPING_THRESHOLD`, and `SHIPPING_FEE`.

| subtotal         | expected        | note     |
| ---------------- | --------------- | -------- |
| Decimal("0.00")  | Decimal("4.99") | edge     |
| Decimal("34.99") | Decimal("4.99") | boundary |
| Decimal("35.00") | Decimal("0.00") | boundary |
| Decimal("35.01") | Decimal("0.00") | boundary |

## `quote_order(quantity, unit_price, member_tier="none", country="US")`

Returns the total the customer pays. Applies the volume and member
discounts one after the other, rounds the subtotal to cents, adds
shipping, then adds tax on the subtotal and shipping and rounds the
total to cents. Both roundings go half up.

Source: docstring and the callables above.

| quantity | unit_price | member_tier | country   | expected                                             | note                                              |
| -------- | ---------- | ----------- | --------- | ---------------------------------------------------- | ------------------------------------------------- |
| 1        | "39.99"    | "none"      | "US"      | Decimal("39.99")                                     | happy, ships free                                 |
| 1        | "20.00"    | "none"      | "US"      | Decimal("24.99")                                     | happy, adds shipping                              |
| 1        | "20.00"    | (omitted)   | (omitted) | Decimal("24.99")                                     | happy, defaults to a US non-member                |
| 1        | "34.99"    | "none"      | "US"      | Decimal("39.98")                                     | boundary, pays shipping                           |
| 1        | "35.00"    | "none"      | "US"      | Decimal("35.00")                                     | boundary, ships free                              |
| 1        | "0.00"     | "none"      | "US"      | Decimal("4.99")                                      | edge, free book still pays shipping               |
| 10       | "39.99"    | "none"      | "US"      | Decimal("379.91")                                    | happy, volume discount, 379.905 rounds half up    |
| 2        | "20.00"    | "pro"       | "US"      | Decimal("36.00")                                     | happy, member discount, ships free                |
| 2        | "18.00"    | "plus"      | "US"      | Decimal("39.19")                                     | edge, discount drops subtotal below free shipping |
| 1        | "20.00"    | "none"      | "GB"      | Decimal("29.99")                                     | happy, tax applies to shipping too                |
| 1        | "35.50"    | "none"      | "DE"      | Decimal("42.25")                                     | edge, tax rounds half up                          |
| 50       | "10.00"    | "pro"       | "GB"      | Decimal("475.20")                                    | happy, every discount and tax combined            |
| 0        | "10.00"    | "none"      | "US"      | raises ValueError: "quantity must be positive"       | error                                             |
| 1        | "-0.01"    | "none"      | "US"      | raises ValueError: "unit price must not be negative" | error                                             |
| 1        | "10.00"    | "gold"      | "US"      | raises ValueError: "unknown tier: gold"              | error                                             |
| 1        | "10.00"    | "none"      | "FR"      | raises ValueError: "unknown country: FR"             | error                                             |

# `bookstore/catalog.py`

Each record has `isbn`, `title`, `author`, and `price` keys.

## `Catalog(path=None)`

Creates a read-only catalog backed by a JSON file, without reading the
file yet.

Source: class docstring and `DEFAULT_CATALOG_PATH`.

| path                   | expected                                                             | note  |
| ---------------------- | -------------------------------------------------------------------- | ----- |
| (omitted)              | `.books` has the four ISBNs in `bookstore/data/books.json`, in order | happy |
| path to a missing file | no error, and `.path` is that path                                   | edge  |

## `Catalog.books`

Returns every record keyed by ISBN, reading the file on first access.

Source: property docstring.

| given                                 | expected                                                                  | note  |
| ------------------------------------- | ------------------------------------------------------------------------- | ----- |
| file with two records                 | dict of both records keyed by ISBN                                        | happy |
| file with `[]`                        | `{}`                                                                      | edge  |
| `.books` already read, file rewritten | the original records, since the file is read once                         | edge  |
| path to a missing file                | raises FileNotFoundError: "[Errno 2] No such file or directory: '<path>'" | error |

## `Catalog.load()`

Reads and parses the catalog file, and returns the catalog itself.

Source: method docstring.

| given                                 | expected                            | note  |
| ------------------------------------- | ----------------------------------- | ----- |
| a valid catalog file                  | returns the same `Catalog` instance | happy |
| `.books` already read, file rewritten | `.books` has the new records        | happy |

## `Catalog.get(isbn)`

Returns the record for one ISBN.

Source: method docstring.

| given                 | isbn    | expected                             | note  |
| --------------------- | ------- | ------------------------------------ | ----- |
| file with two records | stocked | that record's dict                   | happy |
| file with two records | "000"   | raises KeyError: "unknown isbn: 000" | error |

## `Catalog.price_of(isbn)`

Returns the list price of one book, as stored in the file.

Source: method docstring.

| given                     | isbn    | expected                             | note  |
| ------------------------- | ------- | ------------------------------------ | ----- |
| record with price "39.99" | stocked | "39.99"                              | happy |
| file with two records     | "000"   | raises KeyError: "unknown isbn: 000" | error |

## `Catalog.by_author(author)`

Returns every record by an author, in catalog order.

Source: method docstring.

| given                                    | author      | expected                       | note  |
| ---------------------------------------- | ----------- | ------------------------------ | ----- |
| two books by "Dan Bader", one by another | "Dan Bader" | both records, in catalog order | happy |
| no books by the author                   | "Nobody"    | `[]`                           | edge  |

# `bookstore/inventory.py`

`available` is always `on_hand - reserved`.

## `Inventory(stock=None)`

Creates an inventory that keeps its own copy of the on-hand counts.

Source: class docstring.

| stock                            | expected                  | note  |
| -------------------------------- | ------------------------- | ----- |
| `{"A": 5}`                       | `on_hand("A")` is 5       | happy |
| (omitted)                        | `on_hand("A")` is 0       | edge  |
| `{"A": 5}`, caller then edits it | `on_hand("A")` is still 5 | edge  |

## `Inventory.on_hand(isbn)`

Returns the copies physically in the warehouse.

Source: method docstring.

| given      | isbn | expected | note  |
| ---------- | ---- | -------- | ----- |
| `{"A": 5}` | "A"  | 5        | happy |
| `{"A": 5}` | "B"  | 0        | edge  |

## `Inventory.reserved(isbn)`

Returns the copies held for orders that haven't shipped.

Source: method docstring.

| given      | isbn | expected | note |
| ---------- | ---- | -------- | ---- |
| `{"A": 5}` | "A"  | 0        | edge |

## `Inventory.available(isbn)`

Returns the copies that can still be reserved.

Source: method docstring.

| given      | isbn | expected | note  |
| ---------- | ---- | -------- | ----- |
| `{"A": 5}` | "A"  | 5        | happy |

## `Inventory.reserve(isbn, quantity)`

Holds copies for an order and returns what's left available.

Source: method docstring.

| given                  | isbn | quantity | expected                                             | note     |
| ---------------------- | ---- | -------- | ---------------------------------------------------- | -------- |
| `{"A": 5}`             | "A"  | 2        | returns 3, `reserved("A")` is 2, `on_hand("A")` is 5 | happy    |
| `{"A": 5}`, 2 reserved | "A"  | 1        | returns 2, `reserved("A")` is 3                      | happy    |
| `{"A": 5}`             | "A"  | 5        | returns 0                                            | boundary |
| `{"A": 5}`             | "A"  | 6        | raises ValueError: "only 5 copies of A available"    | boundary |
| `{"A": 5}`, 2 reserved | "A"  | 4        | raises ValueError: "only 3 copies of A available"    | boundary |
| `{"A": 5}`             | "A"  | 0        | raises ValueError: "quantity must be positive"       | error    |
| `{"A": 5}`             | "B"  | 1        | raises KeyError: "unknown isbn: B"                   | error    |

## `Inventory.release(isbn, quantity)`

Returns held copies to the pool and returns what's available.

Source: method docstring.

| given                  | isbn | quantity | expected                                               | note     |
| ---------------------- | ---- | -------- | ------------------------------------------------------ | -------- |
| `{"A": 5}`, 3 reserved | "A"  | 1        | returns 3, `reserved("A")` is 2                        | happy    |
| `{"A": 5}`, 3 reserved | "A"  | 3        | returns 5, `reserved("A")` is 0                        | boundary |
| `{"A": 5}`, 3 reserved | "A"  | 4        | raises ValueError: "cannot release 4, only 3 reserved" | boundary |
| `{"A": 5}`             | "A"  | 0        | raises ValueError: "quantity must be positive"         | error    |
| `{"A": 5}`             | "B"  | 1        | raises KeyError: "unknown isbn: B"                     | error    |

## `Inventory.commit(isbn, quantity)`

Ships held copies, removes them from stock, and returns what's on hand.

Source: method docstring.

| given                  | isbn | quantity | expected                                               | note     |
| ---------------------- | ---- | -------- | ------------------------------------------------------ | -------- |
| `{"A": 5}`, 3 reserved | "A"  | 2        | returns 3, `reserved("A")` is 1, `available("A")` is 2 | happy    |
| `{"A": 5}`, 3 reserved | "A"  | 3        | returns 2, `reserved("A")` is 0                        | boundary |
| `{"A": 5}`, 3 reserved | "A"  | 4        | raises ValueError: "cannot ship 4, only 3 reserved"    | boundary |
| `{"A": 5}`             | "A"  | 0        | raises ValueError: "quantity must be positive"         | error    |
| `{"A": 5}`             | "B"  | 1        | raises KeyError: "unknown isbn: B"                     | error    |
