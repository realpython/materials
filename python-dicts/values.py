class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(
    {
        "colors": ["red", "green", "blue"],
        "plugins": {"py_code", "dev_sugar", "fasting_py"},
        "timeout": 3,
        "position": Point(42, 21),
    }
)
