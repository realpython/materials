"""
Optional arguments in Python — consolidated, runnable examples.

This module collects the tutorial's final, good-practice implementations:

- show_list(shopping_list, include_quantities=True)
- add_item(item_name, quantity, shopping_list=None)
- add_items_args(shopping_list, *item_names)
- add_items_kwargs(shopping_list, **things_to_buy)

Run the module directly to see a short demo.
"""


def show_list(shopping_list, include_quantities=True):
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)
    print()


def add_item(item_name, quantity, shopping_list=None):
    """Add (or increment) an item in a list using the safe 'None' default."""
    if shopping_list is None:
        shopping_list = {}
    if item_name in shopping_list:
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity
    return shopping_list


def add_items_args(shopping_list, *item_names):
    """Add any number of item names with default quantity 1 using *args."""
    for item_name in item_names:
        if item_name in shopping_list:
            shopping_list[item_name] += 1
        else:
            shopping_list[item_name] = 1
    return shopping_list


def add_items_kwargs(shopping_list, **things_to_buy):
    """Add any number of items with explicit quantities using **kwargs."""
    for item_name, quantity in things_to_buy.items():
        if item_name in shopping_list:
            shopping_list[item_name] += quantity
        else:
            shopping_list[item_name] = quantity
    return shopping_list


# --- Using required + optional parameters (safe default pattern) ---
hardware_store_list = {}
hardware_store_list = add_item("Nails", 1, hardware_store_list)
hardware_store_list = add_item("Screwdriver", 1, hardware_store_list)
hardware_store_list = add_item("Glue", 3, hardware_store_list)

supermarket_list = {}
supermarket_list = add_item("Bread", 1, supermarket_list)
supermarket_list = add_item("Milk", 2, supermarket_list)

show_list(hardware_store_list)  # With quantities
show_list(supermarket_list, False)  # Names only

# Create new lists on the fly by omitting shopping_list
clothes_shop_list = add_item(
    "Shirt", 3
)  # New dict created inside the function
electronics_store_list = add_item("USB cable", 1)  # New dict created again
show_list(clothes_shop_list)
show_list(electronics_store_list)

# --- Using *args to add many items at once (defaults quantity to 1) ---
multi_add_list = {}
multi_add_list = add_items_args(
    multi_add_list, "Coffee", "Tea", "Cake", "Bread"
)
show_list(multi_add_list)

# --- Using **kwargs to add items with explicit quantities ---
kw_list = {}
kw_list = add_items_kwargs(kw_list, coffee=1, tea=2, cake=1, bread=3)
show_list(kw_list)
