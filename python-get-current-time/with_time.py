import time

# Should prefer using datetime over time

print(
    f"""
{time.time()=}
{time.ctime()}
{time.gmtime()}
{time.localtime()}
"""
)
