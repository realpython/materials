class PlatformException(Exception):
    """Incompatible platform."""


def linux_interaction():
    import sys

    if "linux" not in sys.platform:
        raise PlatformException("Function can only run on Linux systems.")
    print("Doing Linux things.")


try:
    linux_interaction()
except PlatformException as error:
    print(error)
    print("The linux_interaction() function wasn't executed.")
