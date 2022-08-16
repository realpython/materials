import tomllib_w

data = {
    "author": {
        "name": "Geir Arne Hjelle",
        "email": "geirarne@realpython.com",
    },
    "url": "https://realpython.com/python311-tomllib/",
}

print(tomllib_w.dumps(data))
