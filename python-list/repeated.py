def get_unique_items(list_object):
    result = []
    for item in list_object:
        if item not in result:
            result.append(item)
    return result


print(get_unique_items([2, 4, 5, 2, 3, 5]))


def get_unique_items_tail(list_object):
    result = []
    for item in reversed(list_object):
        if item not in result:
            result.insert(0, item)
    return result


print(get_unique_items_tail([2, 4, 5, 2, 3, 5]))
