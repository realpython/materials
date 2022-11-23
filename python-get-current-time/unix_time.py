import datetime
import time

# Should prefer datetime over time
LOCAL_TIMEZONE = (
    datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
)

datetime_unixtime = datetime.datetime.now().timestamp()
time_unixtime = time.time()
timezone_aware_unixtime = datetime.datetime.now(tz=LOCAL_TIMEZONE).timestamp()

print(
    f"""
{datetime_unixtime       = }
{time_unixtime           = }
{timezone_aware_unixtime = }
"""
)

import datetime

LOCAL_TIMEZONE = (
    datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
)

timezone_naive_unixtime = datetime.datetime.now().timestamp()
timezone_aware_unixtime = datetime.datetime.now(tz=LOCAL_TIMEZONE).timestamp()

print(
    f"""
{timezone_naive_unixtime = }
{timezone_aware_unixtime = }
"""
)
