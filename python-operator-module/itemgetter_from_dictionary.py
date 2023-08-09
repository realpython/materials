import operator

musician_dicts = [
    {"id": 1, "fname": "Brian", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 2, "fname": "Carl", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 3, "fname": "Dennis", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 4, "fname": "Bruce", "lname": "Johnston", "group": "Beach Boys"},
    {"id": 5, "fname": "Hank", "lname": "Marvin", "group": "Shadows"},
    {"id": 6, "fname": "Bruce", "lname": "Welch", "group": "Shadows"},
    {"id": 7, "fname": "Brian", "lname": "Bennett", "group": "Shadows"},
]


# Get a single element
get_element_four = operator.itemgetter(4)
print(get_element_four(musician_dicts))

# Get multiple elements
get_elements_one_three_five = operator.itemgetter(1, 3, 5)
print(get_elements_one_three_five(musician_dicts))

# Get values within elements
get_names = operator.itemgetter("fname", "lname")

for musician in get_elements_one_three_five(musician_dicts):
    print(get_names(musician))
