"""
Demonstrates why using a mutable default (like {}) is a bad idea.

This mirrors the tutorial's buggy example so you can reproduce the issue.
Run this file directly to see both variables share the same underlying dict.
"""


def add_item(item_name, quantity, shopping_list={}):
    # BAD: the default dict is created once and reused
    if item_name in shopping_list:
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity
    return shopping_list


clothes_shop_list = add_item("Shirt", 3)  # Uses the shared default dict
electronics_store_list = add_item("USB cable", 1)  # Same shared dict!

print("clothes_shop_list:")
for k, v in clothes_shop_list.items():
    print(f"{v}x {k}")

print("\nelectronics_store_list:")
for k, v in electronics_store_list.items():
    print(f"{v}x {k}")

print(
    "\nNote how both lists contain the same combined items "
    "due to the shared default."
)
