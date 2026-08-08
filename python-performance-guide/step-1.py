import timeit


def count_pairs_slow(numbers, target):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1
    return count


sample = list(range(5_000))
target = 4_999

print(count_pairs_slow(sample, target))

slow_time = timeit.timeit(lambda: count_pairs_slow(sample, target), number=10)
print(f"count_pairs_slow: {slow_time:.4f} seconds")


def count_pairs_fast(numbers, target):
    seen = set()
    count = 0
    for number in numbers:
        complement = target - number
        if complement in seen:
            count += 1
        seen.add(number)
    return count


print(count_pairs_fast(sample, target))

fast_time = timeit.timeit(lambda: count_pairs_fast(sample, target), number=10)
print(f"count_pairs_fast: {fast_time:.4f} seconds")
