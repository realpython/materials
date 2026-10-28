def function():
    x = 10  # noqa: F841
    function()


if __name__ == "__main__":
    function()
