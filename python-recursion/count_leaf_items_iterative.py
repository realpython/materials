from names import names


def count_leaf_items(item_list):
    """Non-recursively counts and returns the
    number of leaf items in a (potentially
    nested) list.
    """
    count = 0
    stack = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1


if __name__ == "__main__":
    print(count_leaf_items([1, 2, 3, 4]))
    print(count_leaf_items([1, [2.1, 2.2], 3]))
    print(count_leaf_items([]))
    print(count_leaf_items(names))
