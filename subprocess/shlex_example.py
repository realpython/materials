"""
Demonstration of using `shlex` to parse a command into tokens that can be
passed to `subrprocess.run()`, for example.
"""

import shlex

print(shlex.split("git commit -m 'first commit'"))
