person = {"name": "Jane Doe", "age": 25}
f"Hello, {person['name']}! You're {person['age']} years old."

"Hello, {name}! You're {age} years old.".format(**person)
"Hello, {name}!".format(**person)

"Hello, %(name)s! You're %(age)s years old." % person
"Hello, %(name)s!" % person
