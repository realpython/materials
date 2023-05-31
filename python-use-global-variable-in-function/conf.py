config = {
    "base_url": "http://127.0.0.1:5000/api",
    "timeout": 30,
}


def update_config(**kwargs):
    for key, value in kwargs.items():
        if key in {"api_key", "base_url", "timeout"}:
            config[key] = value
        else:
            raise KeyError(key)
