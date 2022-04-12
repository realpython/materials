import subprocess

# Variations to do the same thing

ls_process = subprocess.run(["ls"], capture_output=True)
grep_process = subprocess.run(["grep", "basics"], input=ls_process.stdout)

subprocess.run(
    ["grep", "basics"],
    input=subprocess.run(["ls"], capture_output=True).stdout,
)

ls_process = subprocess.run(["ls"], stdout=subprocess.PIPE)
grep_process = subprocess.run(["grep", "basics"], stdin=ls_process.stdout)

# This one doesn't work
print(subprocess.PIPE)  # -1
ls_process = subprocess.run(["ls"], stdout=-1)
print(ls_process.stdout)  # Successfully outputs
grep_process = subprocess.run(
    ["grep", "basics"], stdin=ls_process.stdout  # Why does this not work??
)

piped_process = subprocess.run(["bash", "-c", "ls | grep basic"])


with open("buffer", "w") as buffer:
    ls_process = subprocess.run(["ls"], stdout=buffer)

with open("buffer", "r") as buffer:
    grep_process = subprocess.run(["grep", "basic"], stdin=buffer)
