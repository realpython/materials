def username(fn, ln, /):
    return fn + ln[0]


print(username("Frank", "Sinatra"))

print(username(fn="Frank", ln="Sinatra"))
