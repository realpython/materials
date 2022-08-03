from timeit import timeit
from samples import dictionary_of_dictionaries, list_of_dictionaries

lookups = [15, 18, 19, 16, 6, 12, 5, 3, 9, 20, 2, 10, 13, 17, 4, 14, 11, 7, 8]

list_setup = """
def get_key_from_list(key):
    for item in list_of_dictionaries:
        if item["id"] == key:
            return item
"""

lookup_list = """
for key in lookups:
    get_key_from_list(key)
"""

lookup_dict = """
for key in lookups:
    dictionary_of_dictionaries[key]
"""

lookup_list_time = timeit(
    stmt=lookup_list, setup=list_setup, globals=globals()
)
lookup_dict_time = timeit(stmt=lookup_dict, globals=globals())

print(
    f"""\
{lookup_list_time=:.2f} seconds
{lookup_dict_time=:.2f} seconds
dict is {(lookup_list_time / lookup_dict_time):.2f} times faster"""
)
