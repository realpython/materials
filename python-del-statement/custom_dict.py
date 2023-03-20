class Dict(dict):
    def __delitem__(self, key) -> None:
        print(f"Running .__delitem__() to delete {(key, self[key])}")
        super().__delitem__(key)
