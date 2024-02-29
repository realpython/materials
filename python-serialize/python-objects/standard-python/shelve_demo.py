import shelve

with shelve.open("/tmp/cache.db") as shelf:
    shelf["last_updated"] = 1696846049.8469703
    shelf["user_sessions"] = {
        "jdoe@domain.com": {
            "user_id": 4185395169,
            "roles": {"admin", "editor"},
            "preferences": {"language": "en_US", "dark_theme": False},
        }
    }
    for key, value in shelf.items():
        print(f"['{key}'] = {value}")
