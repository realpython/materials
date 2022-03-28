import subprocess


process = subprocess.run(["python", "simple_react_perf.py"], input="\n\n", text=True)


"""
OUTPUT

Press enter to play
go!
0.0
"""


# process = subprocess.run(["python", "simple_react.py"], input="\n\n", encoding="utf-8")
