from collections.abc import Iterable

from customiterables import CustomIterableThree

for number in CustomIterableThree(4):
    print(number)


isinstance(CustomIterableThree(4), Iterable)
