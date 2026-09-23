planets = frozendict(
    {
        "Mercury": 57_910_000,
        "Venus": 108_200_000,
        "Earth": 149_600_000,
        "Mars": 227_900_000,
        "Jupiter": 778_500_000,
        "Saturn": 1_434_000_000,
        "Uranus": 2_871_000_000,
        "Neptune": 4_495_000_000,
    }
)

for name, distance in planets.items():
    scaled = round(60 * distance / max(planets.values()))
    print(" " * scaled + "\N{RINGED PLANET}", name)
