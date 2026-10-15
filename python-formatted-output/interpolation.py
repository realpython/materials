# print(f"Hello, Pythonista!")
# print(F"Hello, Pythonista!")

# print(f'Single-line f-string with single quotes')
# print(f"Single-line f-string with double quotes")
# print(
#     f'''Multiline triple-quoted f-string
# with single quotes'''
# )
# print(
#     f"""Multiline triple-quoted f-string
# with double quotes"""
# )

site = "Real Python"
print(f"Welcome to {site}!")

quantity = 6
item = "bananas"
price = 1.74
print(f"{quantity} {item} cost ${price * quantity}")

fruits = ["apple", "mango", "grape"]
numbers = {"one": 1, "two": 2}
print(f"First fruit in the list is '{fruits[0]}'")
print(f"Last two fruits in the list are {fruits[-2:]}")
print(f"Dict value for key 'one' is {numbers['one']}")

lang = "Python"
print(f"{{ {lang} }}")

print("{0} {1} cost ${2}".format(6, "bananas", 1.74 * 6))

print("{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}".format("foo", "bar", "baz"))

print("{} {} cost ${}".format(6, "bananas", 1.74 * 6))

print(
    "{quantity} {item} cost ${cost}".format(
        quantity=6, item="bananas", cost=1.74 * 6
    )
)

print("{x} {y} {z}".format(x="foo", y="bar", z="baz"))

print("{x} {y} {z}".format(y="bar", z="baz", x="foo"))
print("{y} {z} {x}".format(x="foo", y="bar", z="baz"))

x = "foo"
y = "bar"
z = "baz"
print("{0} {1} {s}".format(x, y, s=z))
