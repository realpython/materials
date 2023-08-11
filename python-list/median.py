def median(samples):
    n = len(samples)
    middle_index = n // 2
    sorted_samples = sorted(samples)
    # Odd number of values
    if n % 2:
        return sorted_samples[middle_index]
    # Even number of values
    lower, upper = middle_index - 1, middle_index + 1
    return sum(sorted_samples[lower:upper]) / 2
