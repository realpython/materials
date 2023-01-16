# --------------------------------------------------
# How to Add to `PATH` via GUI
# --------------------------------------------------

<#

Once you've located your Python executable, open the Start menu and search
for the _Edit the system environment variables_ entry, which opens up a
_System Properties_ window. In the _Advanced_ tab, click on the button
_Environment Variables_. There you'll see _User_ and _System_ variables,
which you'll be able to edit.

In the section entitled _User Variables_, double-click on the entry that
says _Path_. Another window will pop up showing a list of paths. Click the
_New_ button and paste the path to your Python executable there. Once that's
inserted, select your newly added path and click the _Move Up_ button until
it's at the top.

That's it! You may need to reboot your computer for the changes to take
effect, but you should now be able to call `python` from the command line.

#>

# --------------------------------------------------
# Working With Environment Variables With PowerShell
# --------------------------------------------------

# Set temporary environment variable (only active for current shell session)
PS> $ENV:TEST = "VALUE"

# Set permanent environment variable (need to restart shell to take effect)
PS> [Environment]::SetEnvironmentVariable("TEST", "VALUE", "User")

PS> cd ENV:
PS> ls

<# OUTPUT

Name                           Value
----                           -----
ALLUSERSPROFILE                C:\ProgramData
ANSICON                        166x32766 (166x66)
ANSICON_DEF                    7
APPDATA                        C:\Users\RealPython\AppData\Roaming
AZ_ENABLED                     False
...
TEST                           VALUE
...

#>

# View PATH
PS> (cat ENV:PATH) -Split ";"

<# OUTPUT

C:\Program Files\PowerShell\7
C:\Windows\system32
C:\Windows
C:\Windows\System32\WindowsPowerShell\v1.0\
C:\Windows\System32\OpenSSH\

#>

# Append path to PATH
PS> $ENV:PATH = "$ENV:PATH;C:\new\path"

# Prepend path to PATH
PS> $ENV:PATH = "C:\new\path;$ENV:PATH"