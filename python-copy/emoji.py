import unicodedata


class Emoji:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self._glyph

    @property
    def name(self):
        return unicodedata.name(self._glyph).title()

    @name.setter
    def name(self, value):
        self._glyph = unicodedata.lookup(value)


if __name__ == "__main__":
    emoji = Emoji("tangerine")
    print(emoji)
    emoji.name = "clown face"
    print(emoji)
