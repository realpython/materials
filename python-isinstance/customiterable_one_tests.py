from collections.abc import Iterable

from customiterables import CustomIterableOne

for number in CustomIterableOne(4):
    print(number)


isinstance(CustomIterableOne(4), Iterable)
