def mean():
    samples = []

    def inner_mean(number):
        samples.append(number)
        return sum(samples) / len(samples)

    return inner_mean


sample_means = mean()

print(sample_means(100))
print(sample_means(105))
print(sample_means(101))
print(sample_means(98))
