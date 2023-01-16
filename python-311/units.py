import pathlib

import tomllib

with pathlib.Path("units.toml").open(mode="rb") as file:
    base_units = tomllib.load(file)

units = {}
for unit, unit_info in base_units.items():
    units[unit] = unit_info
    for alias in unit_info["aliases"]:
        units[alias] = unit_info


def to_baseunit(value, from_unit):
    from_info = units[from_unit]
    if "multiplier" not in from_info:
        return (
            value,
            from_info["label"]["singular" if value == 1 else "plural"],
        )

    return to_baseunit(value * from_info["multiplier"], from_info["to_unit"])


print(to_baseunit(7, "s"))
print(to_baseunit(3.11, "minutes"))
print(to_baseunit(14, "days"))
print(to_baseunit(1 / 12, "yr"))
