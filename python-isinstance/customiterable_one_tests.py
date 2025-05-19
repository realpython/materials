from customiterables import CustomIterableOne

for number in CustomIterableOne(4):
    print(number)

from collections.abc import Iterable

isinstance(CustomIterableOne(4), Iterable)
