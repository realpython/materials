class Top:
    pass


class Middle(Top):
    pass


class Bottom(Middle):
    pass


Bottom.mro()
isinstance(Bottom(), Top)
