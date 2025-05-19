from customiterables import CustomIterableTwo

for number in CustomIterableTwo(4):
    print(number)

isinstance(CustomIterableTwo(4), Iterable)
