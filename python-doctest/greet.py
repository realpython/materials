def greet_with_bank_line(name="World"):
    """Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    Hello, Pythonista!
    <BLANKLINE>
    How have you been?
    """
    print(f"Hello, {name}!")
    print()
    print("How have you been?")


def greet_with_raw_docstring(name="World"):
    r"""Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    /== Hello, Pythonista! ==\
    \== How have you been? ==/
    """
    print(f"/== Hello, {name}! ==\\")
    print("\\== How have you been? ==/")


def greet_with_scaped_backslash(name="World"):
    """Print a greeting.

    Usage examples:
    >>> greet("Pythonista")
    /== Hello, Pythonista! ==\\
    \\== How have you been? ==/
    """
    print(f"/== Hello, {name}! ==\\")
    print("\\== How have you been? ==/")
