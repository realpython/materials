likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

while likes:
    print(f"Dictionary length: {len(likes)}")
    item = likes.popitem()
    # Do something with the item here...
    print(f"Item {item} removed")
print("Your dictionary is now empty.")
