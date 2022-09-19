# ------------------------------------
# Add Path to PATH
# ------------------------------------

# Make sure you use the right profile for your system
$ export PATH="<PATH_TO_PYTHON>:$PATH"

# ------------------------------------
# Add Path-Adding Operation to Profile
# ------------------------------------

# Make sure you use the right profile for your system
$ echo export PATH="<PATH_TO_PYTHON>:$PATH" >> ~/.profile
# Reread profile to see effect in same session
$ source ~/.profile

# ------------------------------------
# Filtering Bad Paths from PATH
# ------------------------------------

# View current PATH
$ echo $PATH
# Output:
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/home/realpython/badpython:/usr/bin:
# /sbin:/bin:/usr/games:/usr/local/games

# View on separate lines by replacing colons with newlines
$ echo $PATH | tr ":" "\n"
# Output:
# /usr/local/sbin
# /usr/local/bin
# /usr/sbin
# /home/realpython/badpython
# /usr/bin
# /sbin
# /bin
# /usr/games
# /usr/local/games

# Filter out certain lines with grep -v
$ echo $PATH | tr ":" "\n" | grep -v 'badpython'
# Output:
# /usr/local/sbin
# /usr/local/bin
# /usr/sbin
# /usr/bin
# /sbin
# /bin
# /usr/games
# /usr/local/games

# Replace newlines with colons
$ echo $PATH | tr ":" "\n" | grep -v 'badpython' | tr "\n" ":"
# Output:
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:
# /usr/local/games

# Assign to PATH
$ export PATH=`echo $PATH | tr ":" "\n" | grep -v 'badpython' | tr "\n" ":"`
