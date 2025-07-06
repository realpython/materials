class Game:
    def __init__(self, name, genre, price) -> None:
        self.name = name
        self.genre = genre
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_genre(self) -> str:
        return self.genre

    def get_price(self) -> float:
        return self.price
