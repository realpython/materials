import sys

lazy import noisy_module

print("The lazy import statement has run.")
print("Loaded?", "noisy_module" in sys.modules)

print(noisy_module.VALUE)
print("Loaded?", "noisy_module" in sys.modules)
