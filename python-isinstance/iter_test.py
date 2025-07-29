from player_iterables import (
    PlayersVersionFour,
    PlayersVersionOne,
    PlayersVersionThree,
    PlayersVersionTwo,
)

print(f"{iter(PlayersVersionOne(["Fast Ed", "Slow Jo", "Still Su"])) = }")
print(f"{iter(PlayersVersionTwo(["Fast Ed", "Slow Jo", "Still Su"])) = }")
print(f"{iter(PlayersVersionThree(["Fast Ed", "Slow Jo", "Still Su"])) = }")
print(f"{iter(PlayersVersionFour(["Fast Ed", "Slow Jo", "Still Su"])) = }")
