t = ("foo", "bar", "baz", "qux")

s1, s2, s3, s4 = t
print(s1)
print(s2)
print(s3)
print(s4)

a = "foo"
b = "bar"
# Using a temporary variable
temp = a
a = b
b = temp
print(a, b)

a = "foo"
b = "bar"
# Using unpacking
a, b = b, a
print(a, b)
