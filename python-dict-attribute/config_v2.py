class Config:
    def __init__(self, name):
        self.name = name

    def set_option(self, key, value):
        self.__dict__[key] = value

    def get_option(self, key):
        return self.__dict__.get(key, None)

    def remove_option(self, key):
        if key in self.__dict__:
            del self.__dict__[key]
            # self.__dict__.pop(key)
            print(f"'{key}' removed!")
        else:
            print(f"'{key}' does not exist.")

    def clear(self):
        self.__dict__.clear()
        print("All options removed!")


conf = Config("GUI App")
conf.set_option("theme", "dark")
conf.set_option("size", "200x400")
print(conf.__dict__)
conf.remove_option("size")
print(conf.__dict__)
# conf.remove_option("autosave")  # Raises KeyError
conf.clear()
print(conf.__dict__)
