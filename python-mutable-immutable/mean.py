def cumulative_mean(value, sample=[]):
    sample.append(value)
    return sum(sample) / len(sample)
