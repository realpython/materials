def bubble_sort_list(a_list):
    n = len(a_list)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                is_sorted = False
        if is_sorted:
            break
    return a_list
