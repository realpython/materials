class List(list):
    def __delitem__(self, index):
        print(f"Running .__delitem__() to delete {self[index]}")
        super().__delitem__(index)
