requests = ["first request", "second request", "third request"]

print("\nWith a for-loop")
for request in requests:
    print(f"Handling {request}")


print("\nWith a while-loop")
it = iter(requests)
while True:
    try:
        request = next(it)
    except StopIteration:
        break

    print(f"Handling {request}")
