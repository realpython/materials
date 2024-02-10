from datetime import datetime

now = datetime.now()

print(f"Today is {now:%a %b %d, %Y} and it's {now:%H:%M} hours")
