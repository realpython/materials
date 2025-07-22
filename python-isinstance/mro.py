class Top:
    pass


class Middle(Top):
    pass


class Bottom(Middle):
    pass


Bottom.mro()
print(f"{isinstance(Bottom(), Top) = }")
