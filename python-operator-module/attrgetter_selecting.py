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

# Returning a single attribute.
get_fname = operator.attrgetter("fname")

for person in group_members:
    print(get_fname(person))

# Returning multiple attributes.
get_id_lname = operator.attrgetter("id", "lname")

for person in group_members:
    print(get_id_lname(person))
