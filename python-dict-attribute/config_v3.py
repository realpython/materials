class Config:
    def __init__(self, name):
        self.name = name

    def set_option(self, key, value):
        setattr(self, key, value)

    def get_option(self, key):
        return getattr(self, key, None)

    def remove_option(self, key):
        if hasattr(self, key):
            delattr(self, key)
            print(f"'{key}' removed!")
        else:
            print(f"'{key}' does not exist.")

    def clear(self):
        for key in list(self.__dict__.keys()):
            delattr(self, key)
        print("All options removed!")


conf = Config("GUI App")
conf.set_option("theme", "dark")
conf.set_option("size", "200x400")
print(conf.__dict__)
conf.remove_option("size")
print(conf.__dict__)
conf.remove_option("autosave")  # Raises KeyError
print(conf.__dict__)
conf.clear()
print(conf.__dict__)
