from dataclasses import dataclass


@dataclass
class Musician:
    id: int
    fname: str
    lname: str
    group: str


musicians_list = [
    [1, "Brian", "Wilson", "Beach Boys"],
    [2, "Carl", "Wilson", "Beach Boys"],
    [3, "Dennis", "Wilson", "Beach Boys"],
    [4, "Bruce", "Johnston", "Beach Boys"],
    [5, "Hank", "Marvin", "Shadows"],
    [6, "Bruce", "Welch", "Shadows"],
    [7, "Brian", "Bennett", "Shadows"],
]

group_members = []

for musician in musicians_list:
    group_members.append(Musician(*musician))

import operator

from dataclasses import dataclass


@dataclass
class Musician:
    id: int
    fname: str
    lname: str
    group: str


musicians_list = [
    [1, "Brian", "Wilson", "Beach Boys"],
    [2, "Carl", "Wilson", "Beach Boys"],
    [3, "Dennis", "Wilson", "Beach Boys"],
    [4, "Bruce", "Johnston", "Beach Boys"],
    [5, "Hank", "Marvin", "Shadows"],
    [6, "Bruce", "Welch", "Shadows"],
    [7, "Brian", "Bennett", "Shadows"],
]

group_members = []

for musician in musicians_list:
    group_members.append(Musician(*musician))

import operator

get_id = operator.attrgetter("id")

print(min(group_members, key=get_id))
print(max(group_members, key=get_id))
