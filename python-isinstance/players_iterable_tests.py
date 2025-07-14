from collections.abc import Iterable

from player_iterables import (
    PlayersVersionFour,
    PlayersVersionOne,
    PlayersVersionThree,
    PlayersVersionTwo,
)

for player in PlayersVersionOne(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

print(
    f"{isinstance(PlayersVersionOne(["Fast Ed", "Slow Jo", "Still Su"]), Iterable) = }"
)

print()
for player in PlayersVersionTwo(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

print(
    f"{isinstance(PlayersVersionTwo(["Fast Ed", "Slow Jo", "Still Su"]), Iterable) = }"
)

print()
for player in PlayersVersionThree(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

print(
    f"{isinstance(PlayersVersionThree(["Fast Ed", "Slow Jo", "Still Su"]), Iterable) = }"
)

# This will fail.
print()
for player in PlayersVersionFour(["Fast Ed", "Slow Jo", "Still Su"]):
    print(player)

print(
    f"{isinstance(PlayersVersionFour(["Fast Ed", "Slow Jo", "Still Su"]), Iterable) = }"
)
