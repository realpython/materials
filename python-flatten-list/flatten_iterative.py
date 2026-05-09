def flatten(nested):
    flat = []
    stack = [iter(nested)]
    while stack:
        for item in stack[-1]:
            if isinstance(item, list):
                stack.append(iter(item))
                break
            flat.append(item)
        else:
            stack.pop()
    return flat


flatten([1, [2, [3, [4, [5, 6]]]], 7, [8, 9]])
