a = ["a", "b"]
a.append("c")
print(a)

a = ["a", "c"]
a.insert(1, "b")
print(a)

a = ["a", "b", "c", "d", "e"]
a.remove("b")
print(a)
a.remove("c")
print(a)

a = ["a", "b", "c", "d", "e"]
a.pop()
print(a)
a.pop()
print(a)
