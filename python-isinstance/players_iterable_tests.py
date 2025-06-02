from collections.abc import Iterable

from player_iterables import PlayersFour, PlayersOne, PlayersThree, PlayersTwo

for player in PlayersOne(["Fast Eddy", "Slow Jo", "Static Pat"]):
    print(player)

isinstance(PlayersOne(["Fast Eddy", "Slow Jo", "Static Pat"]), Iterable)

for player in PlayersTwo(["Fast Eddy", "Slow Jo", "Static Pat"]):
    print(player)

isinstance(PlayersTwo(["Fast Eddy", "Slow Jo", "Static Pat"]), Iterable)

isinstance(PlayersThree(["Fast Eddy", "Slow Jo", "Static Pat"]), Iterable)

# This will fail.
for player in PlayersFour(["Fast Eddy", "Slow Jo", "Static Pat"]):
    print(player)
