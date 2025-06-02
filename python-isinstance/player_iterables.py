from collections.abc import Iterable


class PlayersOne(Iterable):
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return iter(self.players)


class PlayersTwo:

    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return iter(self.players)


class PlayersThree:

    def __init__(self, players):
        self.players = players

    def __getitem__(self, index):
        if index >= len(self.players):
            raise IndexError
        return self.players[index]


class PlayersFour:

    def __init__(self, players):
        self.players = players

    def __iter__(self):
        pass
