from collections.abc import MutableMapping


class PizzaMenu(MutableMapping):
    def __init__(self, menu: dict):
        self._menu = {}
        self._first_letters = {}
        for key, value in menu.items():
            first_letter = key[0].lower()
            if first_letter in self._first_letters:
                self._raise_duplicate_key_error(key)
            self._first_letters[first_letter] = key
            self._menu[key] = value

    def _raise_duplicate_key_error(self, key):
        raise ValueError(
            f"'{key}' is invalid. All pizzas must have unique first letters"
        )

    def __getitem__(self, key):
        if key not in self._menu and len(key) > 1:
            raise KeyError(key)
        key = self._first_letters.get(key[0].lower(), key)
        return self._menu[key]

    def __setitem__(self, key, value):
        first_letter = key[0].lower()
        if len(key) == 1:
            key = self._first_letters.get(first_letter, key)
        if key in self._menu:
            self._menu[key] = value
        elif first_letter in self._first_letters:
            self._raise_duplicate_key_error(key)
        else:
            self._first_letters[first_letter] = key
            self._menu[key] = value

    def __delitem__(self, key):
        if key not in self._menu and len(key) > 1:
            raise KeyError(key)
        key = self._first_letters.pop(key[0].lower(), key)
        del self._menu[key]

    def __iter__(self):
        return iter(self._menu)

    def __len__(self):
        return len(self._menu)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._menu})"

    def __str__(self):
        return str(self._menu)

    def __contains__(self, key):
        return key in self._menu
