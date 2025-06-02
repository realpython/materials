from collections.abc import Iterable

from player_iterables import PlayersFour, PlayersOne, PlayersThree, PlayersTwo

iter(PlayersOne(["Fast Eddy", "Slow Jo", "Static Pat"]))

iter(PlayersTwo(["Fast Eddy", "Slow Jo", "Static Pat"]))

iter(PlayersThree(["Fast Eddy", "Slow Jo", "Static Pat"]))

iter(PlayersFour(["Fast Eddy", "Slow Jo", "Static Pat"]))
