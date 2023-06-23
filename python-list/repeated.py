def get_unique_items(a_list):
    result = []
    for item in a_list:
        if item not in result:
            result.append(item)
    return result


print(get_unique_items([2, 4, 5, 2, 3, 5]))


def get_unique_items_tail(a_list):
    result = []
    for item in reversed(a_list):
        if item not in result:
            result.insert(0, item)
    return result


print(get_unique_items_tail([2, 4, 5, 2, 3, 5]))
