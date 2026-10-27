"""A tiny plug-in registry for the report tool's output formats.

Each format module registers itself at import time, which makes these
imports the ones that must stay eager.
"""

FORMATS = {}

def register(name):
    def decorator(func):
        FORMATS[name] = func
        return func

    return decorator

def available():
    return ", ".join(sorted(FORMATS))
