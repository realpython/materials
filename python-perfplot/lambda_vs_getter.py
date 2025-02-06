import operator
import random

import faker
import perfplot

faker.Faker.seed(10)
fake = faker.Faker()


def create_dict(n):
    return {fake.name(): random.randint(10, 200) for _ in range(n)}


def sort_with_lambda(dict_to_sort: dict):
    return sorted(dict_to_sort.items(), key=lambda item: item[1])


def sort_with_itemgetter(dict_to_sort: dict):
    sorted(dict_to_sort.items(), key=operator.itemgetter(1))


perfplot.live(
    setup=lambda n: create_dict(n),
    kernels=[sort_with_lambda, sort_with_itemgetter],
    n_range=[n**2 for n in range(20)],
    equality_check=None,
)

perfplot.live(
    setup=lambda n: create_dict(n),
    kernels=[sort_with_lambda, sort_with_itemgetter],
    n_range=[2**n for n in range(20)],
    equality_check=None,
)
