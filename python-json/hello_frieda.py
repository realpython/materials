import json

dog_data = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": [
        "eating",
        "sleeping",
        "barking",
    ],
    "age": 8,
    "address": {
        "work": None,
        "home": (
            "Berlin",
            "Germany",
        ),
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": [
                "eating",
                "sleeping",
                "reading",
            ],
        },
        {
            "name": "Mitch",
            "hobbies": [
                "running",
                "snacking",
            ],
        },
    ],
}

with open("hello_frieda.json", mode="w") as write_file:
    json.dump(dog_data, write_file)
