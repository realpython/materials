class Pizza:
    def __init__(self, toppings):
        self.toppings = list(toppings)

    def __repr__(self):
        return f"Pizza({self.toppings})"

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    @staticmethod
    def get_size_in_inches(size):
        """Returns an approximate diameter in inches for common sizes."""
        size_map = {"small": 8, "medium": 12, "large": 16}
        return size_map.get(size, "Unknown size")


if __name__ == "__main__":
    a_pizza = Pizza.margherita()
    print(a_pizza, "😋🍕")
