log_line = "2025-01-15 08:45:23 INFO User logged in from IP 10.0.1.1"

date, time, log_level, message = log_line.split(maxsplit=3)

print(f"Date: {date}")
print(f"Time: {time}")
print(f"Log Level: {log_level}")
print(f"Message: {message}")
