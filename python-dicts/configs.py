configs = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}

# Access a value through its key
print(configs["color"])

# Update a value
configs["font"] = "Helvetica"
print(configs)

configs = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_configs = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
configs.update(user_configs)
print(configs)
configs.update([("width", 200), ("api_key", 1234)])
print(configs)
configs.update(color="yellow", script="__main__.py")
print(configs)

default_configs = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_configs = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
configs = default_configs | user_configs
print(configs)

configs = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
user_configs = {
    "path": "/home",
    "color": "red",
    "font": "Arial",
    "position": (200, 100),
}
configs |= user_configs
print(configs)
