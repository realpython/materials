def display_menu(options):
    print("Main Menu:")
    for pos, option in enumerate(options, start=1):
        print(f"{pos}. {option}")


display_menu(["Open", "Save", "Settings", "Quit"])
