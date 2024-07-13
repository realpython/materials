"""
Exploring 'map()' and 'filter()'
"""

original_names = ["Sarah", "Matt", "Jim", "Denise", "Kate", "Andy"]
names = filter(lambda x: ("a" in x) or ("A" in x), original_names)
names = filter(lambda x: len(x) == 4, names)
names = map(str.upper, names)

print(list(names))
