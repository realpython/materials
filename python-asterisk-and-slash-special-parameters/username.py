def username(fn, ln, /):
    return fn + ln[0]


print(username("Frank", "Sinatra"))

# This would be invalid:
# print(username(fn="Frank", ln="Sinatra"))
