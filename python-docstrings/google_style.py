def get_magic_items(user_id, include_potions=False):
    """
    Retrieve a list of magical items for a specific user.

    Args:
        user_id (int): The ID of the user whose items should be retrieved.
        include_potions (bool, optional): Whether to include potions.

    Returns:
        list[str]: A list of item names associated with the user.
    """
    items = ["wand", "cloak", "crystal ball"]
    if include_potions:
        items.extend(["healing potion", "invisibility potion"])
    return items
