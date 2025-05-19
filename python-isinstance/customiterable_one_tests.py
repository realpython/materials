from customiterables import CustomIterableOne
from collections.abc import Iterable


for number in CustomIterableOne(4):
    print(number)


isinstance(CustomIterableOne(4), Iterable)
