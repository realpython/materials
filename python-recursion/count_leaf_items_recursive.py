from names import names


def count_leaf_items(item_list):
    """Recursively counts and returns the
    number of leaf items in a (potentially
    nested) list.
    """
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1

    return count


if __name__ == "__main__":
    print(count_leaf_items([1, 2, 3, 4]))
    print(count_leaf_items([1, [2.1, 2.2], 3]))
    print(count_leaf_items([]))
    print(count_leaf_items(names))
