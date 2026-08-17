import timeit

words = [
    "apple", "pear", "apple", "cherry", "pear", "apple"
] * 1000

def manual_count(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

print(manual_count(words))

manual_time = timeit.timeit(lambda: manual_count(words), number=1000)
print(f"manual loop: {manual_time:.4f} seconds")