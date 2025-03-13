config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}

# Access a value through its key
print(config["color"])

# Update a value
config["font"] = "Helvetica"
print(config)

config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_config = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
config.update(user_config)
print(config)
config.update([("width", 200), ("api_key", 1234)])
print(config)
config.update(color="yellow", script="__main__.py")
print(config)

default_config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_config = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
config = default_config | user_config
print(config)

config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_config = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
config |= user_config
print(config)
