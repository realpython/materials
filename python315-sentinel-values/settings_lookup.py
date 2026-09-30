import tomllib

from settings_legacy import get_setting

with open("settings.toml", mode="rb") as file:
    config = tomllib.load(file)

print(config)
print(get_setting(config, "db.timeout"))
print(get_setting(config, "db.port", default=5432))
# This lookup intentionally fails because the path doesn't exist.
try:
    get_setting(config, "db.port")
except KeyError as error:
    print(f"Expected KeyError: {error}")
