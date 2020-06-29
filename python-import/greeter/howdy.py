# greeter/howdy.py
import plugins


@plugins.register
def greet(name):
    print(f"Howdy good {name}, honored to meet you!")
