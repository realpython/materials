import re

log_line = "2025-01-15 08:45:23 INFO User logged in from IP 10.0.1.1"
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s(\w+)\s"
components = re.split(pattern, log_line)

print(components)
