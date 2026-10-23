def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# Press Ctrl+C to stop the loop
for i in infinite_sequence():
    print(i, end=" ")
