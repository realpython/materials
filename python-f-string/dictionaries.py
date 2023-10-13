person = {"name": "Jane Doe", "age": 25}

print(f"Hello, {person['name']}! You're {person['age']} years old.")

print("Hello, {name}! You're {age} years old.".format(**person))
print("Hello, {name}!".format(**person))

print("Hello, %(name)s! You're %(age)s years old." % person)
print("Hello, %(name)s!" % person)
