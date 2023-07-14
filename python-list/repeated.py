def get_unique_items(list_object):
    result = []
    for item in list_object:
        if item not in result:
            result.append(item)
    return result


# Faster but requires more memory:
#
# def get_unique_items(list_object):
#     result = []
#     unique_items = set()
#     for item in list_object:
#         if item not in unique_items:
#             result.append(item)
#             unique_items.add(item)
#     return result
