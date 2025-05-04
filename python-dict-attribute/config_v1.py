class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    update = __init__

    def __str__(self):
        return str(self.__dict__)


config = Config(theme="light", font_size=12, language="English")
print(config)

user = {"theme": "dark", "font_size": 14, "language": "Spanish"}
config.update(**user)
print(config)
