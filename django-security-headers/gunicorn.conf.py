"""Gunicorn config file
https://docs.gunicorn.org/en/latest/configure.html
"""

import multiprocessing

# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1

# The socket to bind
bind = "0.0.0.0:8000"
