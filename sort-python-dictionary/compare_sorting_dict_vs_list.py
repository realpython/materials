from timeit import timeit

sorting_list = "sorted(list_of_dictionaries, key=lambda item:item['age'])"
sorting_dict = """
dict(
    sorted(
        dictionary_of_dictionaries.items(), key=lambda item: item[1]['age']
    )
)
"""

sorting_list_time = timeit(
    stmt=sorting_list,
    setup="from samples import list_of_dictionaries",
    globals=globals(),
)
sorting_dict_time = timeit(
    stmt=sorting_dict,
    setup="from samples import dictionary_of_dictionaries",
    globals=globals(),
)

print(
    f"""\
{sorting_list_time=:.2f} seconds
{sorting_dict_time=:.2f} seconds
list is {(sorting_dict_time / sorting_list_time):.2f} times faster"""
)
