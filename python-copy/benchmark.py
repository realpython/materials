from copy import copy
from random import choices, randint
from string import ascii_letters
from timeit import timeit

EXECUTIONS = 10_000
SIZE = 1_000


def main():
    print(f" Size={SIZE:,} ({EXECUTIONS:,}x) ".center(50, "="))
    for container_type in random_dict, random_set, random_list:
        container = container_type(size=SIZE)
        for method, seconds in benchmark(container, EXECUTIONS).items():
            print(f"{seconds:.5f} {method}")
        print()


def benchmark(container, executions):
    type_ = type(container)
    name = type_.__name__
    results = {
        f"{name}.copy()": timeit(container.copy, number=executions),
        f"{name}()": timeit(lambda: type_(container), number=executions),
        f"copy({name})": timeit(lambda: copy(container), number=executions),
    }
    if sliceable(container):
        results[f"{name}[:]"] = timeit(lambda: container[:], number=executions)
    return results


def sliceable(instance):
    try:
        instance[0:1]
    except (TypeError, KeyError):
        return False
    else:
        return True


def random_dict(size):
    keys = random_set(size)
    values = random_set(size)
    return dict(zip(keys, values))


def random_set(size):
    return set(random_list(size))


def random_list(size, shortest=3, longest=15):
    return [
        "".join(choices(ascii_letters, k=randint(shortest, longest)))
        for _ in range(size)
    ]


if __name__ == "__main__":
    main()
