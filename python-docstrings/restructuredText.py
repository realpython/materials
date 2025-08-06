def cast_spell(wand, incantation, target=None):
    """
    Cast a magical spell using a wand and incantation.
    This function simulates casting a spell. With no
    target specified, it is cast into the void.

    :param wand: The wand used to do the spell-casting deed.
    :type wand: str
    :param incantation: The words said to activate the magic.
    :type incantation: str
    :param target: The object or person the spell is directed at (optional).
    :return: A string describing the result of the spell.
    :rtype: str

    :raises ValueError: If the incantation is unknown or the wand fails to work.
    """
    valid_incantations = ["Lumos", "Alohomora", "Expelliarmus"]
    if not wand:
        raise ValueError("You can't cast spells without a wand!")
    if incantation not in valid_incantations:
        raise ValueError("Incantation not recognized.")
    if target:
        return f"{incantation} hits {target} with magic speed!"
    return f"{incantation} is cast into the void...sparkles shimmer faintly"
