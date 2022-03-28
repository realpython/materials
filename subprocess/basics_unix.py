import subprocess

# LINUX examples

subprocess.run("ls")
subprocess.run("bash ls")
subprocess.run(["bash", "ls"])
subprocess.run(["sh", "ls"])
subprocess.run(["zsh", "ls"])
subprocess.run(["ls"])

subprocess.run("python helloworld.py")
