def enchant_wand(wand_type, level=1):
    """
    Enhance a wand with magical properties.

    Args:
        wand_type (str): The type of wand to enchant.
        level (int, optional): The enchantment level. Defaults to 1.

    Returns:
        str: A message confirming the enchantment.

    Raises:
        ValueError: If the enchantment level is invalid.
    """
    if level < 1:
        raise ValueError("Enchantment level must be at least 1.")
    return f"{wand_type.title()} enchanted to level {level}!"
