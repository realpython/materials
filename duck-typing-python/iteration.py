numbers = [1, 2, 3]
person = ("Jane", 25, "Python Dev")
letters = "abc"
ordinals = {"one": "first", "two": "second", "three": "third"}
even_digits = {2, 4, 6, 8}
collections = [numbers, person, letters, ordinals, even_digits]

for collection in collections:
    for value in collection:
        print(value)
