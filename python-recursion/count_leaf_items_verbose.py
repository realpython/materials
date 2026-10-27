from names import names


def count_leaf_items(item_list):
    """Recursively counts and returns the
    number of leaf items in a (potentially
    nested) list.
    """
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += count_leaf_items(item)
        else:
            print(f'Counted leaf item "{item}"')
            count += 1

    print(f"-> Returning count {count}")
    return count


if __name__ == "__main__":
    print(count_leaf_items(names))
