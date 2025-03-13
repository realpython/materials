class Config:
    def __init__(self, name):
        self.name = name

    def set_option(self, key, value):
        setattr(self, key, value)

    def get_option(self, key):
        return getattr(self, key, None)

    def remove_option(self, key):
        if key in self.__dict__:
            delattr(self, key)
            print(f"'{key}' removed!")
        else:
            print(f"'{key}' does not exist.")

    def clear(self):
        for key in self.__dict__:
            delattr(self, key)
        print("All options removed!")
