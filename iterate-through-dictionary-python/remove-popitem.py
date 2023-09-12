likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

while True:
    try:
        print(f"Dictionary length: {len(likes)}")
        item = likes.popitem()
        # Do something with the item here...
        print(f"Item {item} removed")
    except KeyError:
        print("Your dictionary is now empty.")
        break
