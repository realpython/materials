import operator
from dataclasses import dataclass


@dataclass
class Musician:
    id: int
    fname: str
    lname: str
    group: str


musician_lists = [
    [1, "Brian", "Wilson", "Beach Boys"],
    [2, "Carl", "Wilson", "Beach Boys"],
    [3, "Dennis", "Wilson", "Beach Boys"],
    [4, "Bruce", "Johnston", "Beach Boys"],
    [5, "Hank", "Marvin", "Shadows"],
    [6, "Bruce", "Welch", "Shadows"],
    [7, "Brian", "Bennett", "Shadows"],
]

group_members = []

for musician in musician_lists:
    group_members.append(Musician(*musician))

# Sorting on a single attribute.

get_id = operator.attrgetter("id")
for musician in sorted(group_members, key=get_id, reverse=True):
    print(musician)
