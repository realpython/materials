"""
**Only works on Windows**

Demonstrates basic usage of `subprocess.run()`.
"""

import subprocess

# https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd
subprocess.run("dir", shell=True)  # COMSPEC env variable
subprocess.run(["cmd.exe", "/c", "dir"])

# https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.2
subprocess.run(["powershell", "-Command", "ls"])
subprocess.run(["python", "helloworld.py"])
