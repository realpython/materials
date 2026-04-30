def flatten(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


nested = [1, [2, [3, [4, [5, 6]]]], 7, [8, 9]]
flatten(nested)
