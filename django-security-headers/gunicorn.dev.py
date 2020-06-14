"""Gunicorn *development* config file
https://docs.gunicorn.org/en/latest/configure.html
"""

# The granularity of Error log outputs
log_level = "debug"

# The number of worker processes for handling requests
workers = 2

# The socket to bind
bind = "0.0.0.0:8000"

# Restart workers when code changes (development only!)
reload = True
