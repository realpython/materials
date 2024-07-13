def list_menu(options):
    print("Main Menu:")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")


# Example usage
menu_options = ["Open", "Save", "Settings", "Quit"]
list_menu(menu_options)
