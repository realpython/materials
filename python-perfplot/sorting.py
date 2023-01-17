from random import randint

import perfplot


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:])
    )


def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


def insertion_sort_tim(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


def timsort(array):
    min_run = 32
    n = len(array)
    for i in range(0, n, min_run):
        insertion_sort_tim(array, i, min((i + min_run - 1), n - 1))
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(
                left=array[start : midpoint + 1],
                right=array[midpoint + 1 : end + 1],
            )
            array[start : start + len(merged_array)] = merged_array
        size *= 2
    return array


def python_built_in(array):
    return sorted(array)


# perfplot.show(
#     setup=lambda n: [randint(0, 1000) for _ in range(n)],
#     kernels=[
#         bubble_sort,
#         insertion_sort,
#         merge_sort,
#         quicksort,
#         timsort,
#         python_built_in,
#     ],
#     n_range=list(range(0, 10000, 1000)),
# )

# perfplot.show(
#     setup=lambda n: [randint(0, 1000) for _ in range(n)],
#     kernels=[
#         bubble_sort,
#         insertion_sort,
#         merge_sort,
#         quicksort,
#         timsort,
#         python_built_in,
#     ],
#     n_range=[2**n for n in range(15)],
# )


# perfplot.show(
#     setup=lambda n: list(range(n)),
#     kernels=[
#         bubble_sort,
#         insertion_sort,
#         merge_sort,
#         quicksort,
#         timsort,
#         python_built_in,
#     ],
#     n_range=[2**n for n in range(15)],
# )

# perfplot.show(
#     setup=lambda n: [n + 1, *list(range(n))],
#     kernels=[
#         bubble_sort,
#         insertion_sort,
#         merge_sort,
#         quicksort,
#         timsort,
#         python_built_in,
#     ],
#     n_range=[2**n for n in range(15)],
# )

plot = perfplot.bench(
    setup=lambda n: [n + 1, *list(range(n))],
    kernels=[
        bubble_sort,
        insertion_sort,
        merge_sort,
        quicksort,
        timsort,
        python_built_in,
    ],
    n_range=[2**n for n in range(10)],
)

plot.show(logx=False, logy=True)
plot.save("sorting.png", logx=False, logy=True)
