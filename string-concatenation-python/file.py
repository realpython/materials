words = ["Hello,", "World!", "I", "am", "a", "Pythonista!"]

with open("output.txt", "w") as f:
    print(*words, sep="\n", file=f)
