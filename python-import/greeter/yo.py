# greeter/yo.py
import plugins


@plugins.register
def greet(name):
    print(f"Yo {name}, good times!")
