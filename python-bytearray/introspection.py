def main():
    print(
        "Mutator methods in bytearray:",
        sorted(public_members(bytearray) - public_members(bytes)),
    )
    print(
        "Special methods in bytearray:",
        sorted(magic_members(bytearray) - magic_members(bytes)),
    )
    show_string_members()


def public_members(cls):
    return {name for name in dir(cls) if not name.startswith("_")}


def magic_members(cls):
    return {name for name in dir(cls) if name.startswith("__")}


def show_string_members():
    print("String members in bytearray:")
    for i, name in enumerate(
        sorted(
            name
            for name in set(dir(bytearray)) & set(dir(str))
            if not name.startswith("_")
        ),
        start=1,
    ):
        print(f"({i:>2}) .{name}()")


if __name__ == "__main__":
    main()
