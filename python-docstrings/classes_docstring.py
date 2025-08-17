class Potion:
    """
    Represents a magical potion composed of various ingredients.

    Attributes
    ----------
    name : str
        The name of the potion.
    ingredients : list of str
        A list of ingredients used in the potion.
    potency : int
        The strength level of the potion.

    Methods
    -------
    brew():
        Completes the potion and sets its potency.
    describe():
        Returns a human-readable summary of the potion.
    """

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.potency = 0

    def brew(self):
        """Simulate brewing the potion by calculating potency."""
        self.potency = len(self.ingredients) * 10

    def describe(self):
        """Return a string describing the potion and its strength."""
        return f"{self.name} (Potency: {self.potency})"
