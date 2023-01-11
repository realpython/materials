people = [
    ["name", "age", "job"],
    ["Stephanie Gould", 100, "Banker"],
    ["Christopher Ward", 115, "Doctor, general practice"],
    ["Jill Santiago", 80, "Insurance account manager"],
    ["John Lewis", 58, "Animal technologist"],
    ["Bianca Moore", 39, "Plant breeder/geneticist"],
]


for row in people[1:]:
    print(row)

import pandas as pd

people = pd.DataFrame(people[1:], columns=people[0])

print(people)

for row in people:
    print(row)

for row in people.itertuples():
    print(row)

for row in people.itertuples():
    print(f"{row[1]} is a {row.job}")

people = [
    [
        "name",
        "Stephanie Gould",
        "Christopher Ward",
        "Jill Santiago",
        "John Lewis",
        "Bianca Moore",
    ],
    ["age", 44, 85, 27, 21, 112],
    [
        "job",
        "Banker",
        "Doctor, general practice",
        "Insurance account manager",
        "Animal technologist",
        "Plant breeder/geneticist",
    ],
]
