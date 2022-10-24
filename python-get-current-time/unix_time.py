import datetime
import time

# Should prefer datetime over time

datetime_unixtime = datetime.datetime.now().timestamp()
time_unixtime = time.time()

print(
    f"""
{datetime_unixtime=}
{time_unixtime=}
"""
)
