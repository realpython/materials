# Avoid this:
# def total_length(items):
#     result = 0
#     if isinstance(items, list):
#         for i in range(len(items)):
#             result += len(items[i])
#     return result


# Favor this:
def total_length(items):
    return sum(len(item) for item in items)
