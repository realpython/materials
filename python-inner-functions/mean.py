def mean():
    sample = []

    def inner_mean(number):
        sample.append(number)
        return sum(sample) / len(sample)

    return inner_mean


sample_mean = mean()

print(sample_mean(100))
print(sample_mean(105))
print(sample_mean(101))
print(sample_mean(98))
