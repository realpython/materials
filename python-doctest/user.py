class User_One:
    def __init__(self, name, favorite_colors):
        self.name = name
        self._favorite_colors = set(favorite_colors)

    @property
    def favorite_colors(self):
        """Return the user's favorite colors.

        Usage examples:
        >>> john = User("John", {"#797EF6", "#4ADEDE", "#1AA7EC"})
        >>> john.favorite_colors
        {'#1AA7EC', '#4ADEDE', '#797EF6'}
        """
        return self._favorite_colors


class User_Two:
    def __init__(self, name, favorite_colors):
        self.name = name
        self._favorite_colors = set(favorite_colors)

    @property
    def favorite_colors(self):
        """Return the user's favorite colors.

        Usage examples:
        >>> john = User("John", {"#797EF6", "#4ADEDE", "#1AA7EC"})
        >>> sorted(john.favorite_colors)
        ['#1AA7EC', '#4ADEDE', '#797EF6']
        """
        return self._favorite_colors


class User_Three:
    def __init__(self, name, favorite_colors):
        """Initialize instances of User.

        Usage examples:
        >>> User(
        ...     "John", {"#797EF6", "#4ADEDE", "#1AA7EC"}
        ... ) # doctest: +ELLIPSIS
        <sets.User object at 0x...>
        """
        self.name = name
        self._favorite_colors = set(favorite_colors)
