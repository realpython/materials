class AlienPet:
    def __init__(self, name):
        self.name = name
        self.fed_level = 0
        self.rested_level = 0
        self.MAX_STATUS = 10

    def feed(self):
        """Increments the feeding level."""
        if self.fed_level < self.MAX_STATUS:
            self.fed_level += 1

    def rest(self):
        """Increments the rested level."""
        if self.rested_level < self.MAX_STATUS:
            self.rested_level += 1

    def is_happy(self) -> bool:
        """The pet is genuinely happy only when fully fed and rested."""
        return (
            self.fed_level == self.MAX_STATUS
            and self.rested_level == self.MAX_STATUS
        )

    def get_status(self) -> str:
        if self.is_happy():
            return "🛸 Happy and thriving!"
        if self.fed_level < 5:
            return "👾 Starving! Please feed me."
        return "Doing okay, but still feels a bit empty..."
