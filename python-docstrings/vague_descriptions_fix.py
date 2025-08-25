def brew(potion_ingredients):
    """
    Mixes the provided ingredients to brew a potion.

    Args:
        potion_ingredients (list of str): Ingredients needed to brew the potion.

    Returns:
        str: The name of the completed potion.
    """
    return f"Magical potion brewed from {', '.join(potion_ingredients)}"
