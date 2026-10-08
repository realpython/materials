# Heads-up: the tutorial runs these examples in the REPL, where each
# statement is compiled on its own, so the two 1001 literals below become two
# separate objects and x is y is False. In a script, Python compiles the whole
# module at once and reuses a single 1001 object for both names, so this file
# prints True where the tutorial prints False. The equality results and the
# string examples are the same either way.

x = 1001
y = 1001

print(x == y)
print(x is y)

# The id() numbers differ on every machine and every run
print(id(x))
print(id(y))

a = "Hello, Pythonista!"
b = a

print(id(a))
print(id(b))

print(a is b)

# The is not operator is the opposite of is
x = 1001
y = 1001
print(x is not y)

a = "Hello, Pythonista!"
b = a
print(a is not b)
