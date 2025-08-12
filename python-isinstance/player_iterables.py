from collections.abc import Iterable


class PlayersVersionOne(Iterable):
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return iter(self.players)


class PlayersVersionTwo:
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        return iter(self.players)


class PlayersVersionThree:
    def __init__(self, players):
        self.players = players

    def __getitem__(self, index):
        if index >= len(self.players):
            raise IndexError
        return self.players[index]


class PlayersVersionFour:
    def __init__(self, players):
        self.players = players

    def __iter__(self):
        pass
