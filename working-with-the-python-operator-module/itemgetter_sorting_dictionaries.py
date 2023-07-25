musicians = [
    {"id": 1, "fname": "Brian", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 2, "fname": "Carl", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 3, "fname": "Dennis", "lname": "Wilson", "group": "Beach Boys"},
    {"id": 4, "fname": "Bruce", "lname": "Johnston", "group": "Beach Boys"},
    {"id": 5, "fname": "Hank", "lname": "Marvin", "group": "Shadows"},
    {"id": 6, "fname": "Bruce", "lname": "Welch", "group": "Shadows"},
    {"id": 7, "fname": "Brian", "lname": "Bennett", "group": "Shadows"},
]

import operator

get_names = operator.itemgetter("lname", "fname")
print(sorted(musicians, key=get_names, reverse=True))
