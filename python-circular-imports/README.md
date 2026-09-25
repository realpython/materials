# Python Circular Imports: Why They Happen and How to Fix Them

This folder provides the code examples for the Real Python tutorial [Python Circular Imports: Why They Happen and How to Fix Them](https://realpython.com/python-circular-imports/)

Everything here is standard library only. The examples target **Python 3.14**, which evaluates annotations lazily. Where a result differs on older versions, the table below says so.

Each folder is a self-contained project with the same layout. Run it from inside that folder:

```console
$ cd broken/
$ python main.py
```

## What's Here

| Path | Section | Result |
| --- | --- | --- |
| `broken/` | A Python Circular Imports Example | `ImportError` |
| `step1_remove_dependency/` | Step 1: Remove the Runtime Dependency | `2004.99` on 3.14, `NameError` on 3.13 and earlier |
| `step2_guard_annotation/` | Step 2: Guard the Type-Only Import | `2004.99` |
| `workaround1_defer_import/` | 1. Defer Imports to Inside Functions | `1004.99` |
| `workaround2_bottom_import/` | 2. Move Imports to the Bottom | `1004.99` |
| `workaround3_attribute_error/` | 3. Change How You Import the Module | `AttributeError` |
| `workaround3_import_module/` | 3. Change How You Import the Module | `1004.99` |

Two folders fail on purpose. `broken/` is the circular import the tutorial sets out to fix, and `workaround3_attribute_error/` shows what happens when a module-level line reaches for a class that isn't defined yet.

## Notes on the Linting

Two files carry a `# noqa` comment, because the tutorial is deliberately showing code that a linter would object to:

- `step1_remove_dependency/shop/product.py` annotates with `Order` while no import provides it. That is exactly the gap Step 2 closes, so the annotation stays unresolved here.
- `workaround2_bottom_import/shop/product.py` puts an import at the bottom of the file, which is the technique that section demonstrates.

## Import Order

The workarounds behave differently depending on which module is imported first. Every `main.py` here imports `shop.product` first. Change that to `shop.order` and both `workaround2_bottom_import/` and `workaround3_import_module/` raise `ImportError` again, while `workaround1_defer_import/` keeps working.
