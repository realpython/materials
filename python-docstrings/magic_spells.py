def undo_spell(spell):
    """
    Reverses characters in a spell incantation, thereby undoing a spell.

    Example:
    >>> undo_spell("Expelliarmus")
    'sumraillepxE'

    >>> undo_spell("Lumos")
    'somuL'
    """
    return spell[::-1]
