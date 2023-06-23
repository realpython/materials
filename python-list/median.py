def median(sample):
    n = len(sample)
    index = n // 2
    sorted_sample = sorted(sample)
    # Odd number of values
    if n % 2 != 0:
        return sorted_sample[index]
    # Even number of values
    lower, upper = index - 1, index + 1
    return sum(sorted_sample[lower:upper]) / 2
