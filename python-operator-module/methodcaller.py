import operator
from dataclasses import dataclass


@dataclass
class Musician:
    id: int
    fname: str
    lname: str
    group: str

    def get_full_name(self, last_name_first=False):
        if last_name_first:
            return f"{self.lname}, {self.fname}"
        return f"{self.fname} {self.lname}"


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

# Print first name, then last name.
first_last = operator.methodcaller("get_full_name")

for person in group_members:
    print(first_last(person))

# Print last name, then first name.
last_first = operator.methodcaller("get_full_name", True)
print("\n")
for person in group_members:
    print(last_first(person))
