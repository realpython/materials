john_friends = {"Linda", "Mathew", "Carlos", "Laura"}
jane_friends = {"Alice", "Bob", "Laura", "Mathew"}

print(john_friends & jane_friends)
print(john_friends.intersection(jane_friends))

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

print(a & b & c & d)
print(a.intersection(b, c, d))
