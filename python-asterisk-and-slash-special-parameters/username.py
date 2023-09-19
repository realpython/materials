def username(fn, ln, /):
    return ln + fn[0]


print(username("Frank", "Sinatra"))

# This would be invalid:
# print(username(fn="Frank", ln="Sinatra"))
