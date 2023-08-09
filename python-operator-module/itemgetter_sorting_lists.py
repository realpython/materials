import operator

musician_lists = [
    [1, "Brian", "Wilson", "Beach Boys"],
    [2, "Carl", "Wilson", "Beach Boys"],
    [3, "Dennis", "Wilson", "Beach Boys"],
    [4, "Bruce", "Johnston", "Beach Boys"],
    [5, "Hank", "Marvin", "Shadows"],
    [6, "Bruce", "Welch", "Shadows"],
    [7, "Brian", "Bennett", "Shadows"],
]

get_id = operator.itemgetter(0)
print(sorted(musician_lists, key=get_id, reverse=True))

get_elements_two_one = operator.itemgetter(2, 1)
print(sorted(musician_lists, key=get_elements_two_one, reverse=True))
