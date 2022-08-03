from timeit import timeit
from samples import dictionary_of_dictionaries, list_of_dictionaries

list_program = "sorted(list_of_dictionaries, key=lambda item:item['age'])"
dict_program = """
dict(
    sorted(
        dictionary_of_dictionaries.items(), key=lambda item: item[1]['age']
    )
)
"""

list_time = timeit(stmt=list_program, globals=globals())
dict_time = timeit(stmt=dict_program, globals=globals())

print(
    f"""
{list_time=:.2f} seconds
{dict_time=:.2f} seconds
list is {(dict_time/list_time):.2f} times faster
"""
)
