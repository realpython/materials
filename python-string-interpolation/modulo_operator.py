name = "Pythonista"
day = "Friday"  # Of course 😃

print("Hello, %s! Today is %s." % (name, day))

x = 5
y = 10
print("The sum of %s and %s is %s." % (x, y, x + y))

template = "The sum of %s and %s is %s."
print(template % (x, y, x + y))

print("Hello, %s!" % "Pythonista")
print("Hello, %s!" % ("Pythonista",))

# print("Interpolating a tuple: %s" % (1, 2, 3))
print("Interpolating a tuple: %s" % ((1, 2, 3),))

jane = {"name": "Jane", "job": "Python Dev"}
print("My name is %(name)s. I'm a %(job)s." % jane)
