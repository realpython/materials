from collections.abc import Iterable

from player_iterables import (
    PlayersVersionOne,
    PlayersVersionTwo,
    PlayersVersionThree,
    PlayersVersionFour,
)

for player in PlayersVersionOne(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

isinstance(PlayersVersionOne(["Fast Ed", "Slow Jo", "Still Su"]), Iterable)

for player in PlayersVersionTwo(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

isinstance(PlayersVersionTwo(["Fast Ed", "Slow Jo", "Still Su"]), Iterable)

for player in PlayersVersionThree(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

isinstance(PlayersVersionThree(["Fast Ed", "Slow Jo", "Still Su"]), Iterable)

# This will fail.
for player in PlayersVersionFour(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

isinstance(PlayersVersionFour(["Fast Ed", "Slow Jo", "Still Su"]), Iterable)
