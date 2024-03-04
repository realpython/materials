print("Name at least 3 colors in the Kenyan flag.")

kenya_flag_colors = {"green", "black", "red", "white"}
user_colors = set()

while len(user_colors) < 3:
    color = input("Enter a color on the Kenya flag: ")
    user_colors.add(color.lower())

if user_colors.issubset(kenya_flag_colors):
    print(
        "Correct! These colors are all in the Kenyan flag: "
        + ", ".join(user_colors)
    )
else:
    print(
        "Incorrect. The colors of the Kenyan flag are: "
        + ", ".join(kenya_flag_colors)
    )
