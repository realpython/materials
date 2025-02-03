log_data = """2025-01-15 08:45:23 INFO User logged in
2025-01-15 09:15:42 ERROR Failed to connect to server
2025-01-15 10:01:05 WARNING Disk space running low"""

log_lines = log_data.splitlines()

for line in log_lines:
    if "ERROR" in line:
        print(line)
