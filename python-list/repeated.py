def get_unique_items(list_object):
    result = []
    for item in list_object:
        if item not in result:
            result.append(item)
    return result
