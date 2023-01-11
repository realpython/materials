import random

from faker import Faker

fake = Faker()
Faker.seed(2)

people = [
    ["name", "age", "job"],
    *[
        [
            f"{fake.first_name()} {fake.last_name()}",
            random.randint(18, 120),
            fake.job(),
        ]
        for _ in range(5)
    ],
]

print(people)

people_transposed = list(map(list, zip(*people)))

print(people_transposed)
