def capitalize_fruit_names(fruits):
    capitalized_fruit_names = []
    cleaned = [fruit if isinstance(fruit, str) else "" for fruit in fruits]

    for fruit in cleaned:
        capitalized_fruit_names.append(fruit.capitalize())

    return capitalized_fruit_names


if __name__ == "__main__":
    print(capitalize_fruit_names(["apple", "BANANA", "cherry", "maNgo"]))
