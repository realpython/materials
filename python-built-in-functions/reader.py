def read_user_input():
    print("Enter word (type 'done' to finish):")
    for word in iter(input, "done"):
        print(f"Processing word: '{word}'")


read_user_input()
