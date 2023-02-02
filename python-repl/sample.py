def read_data():
    # Read data from a file or database...
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sample = read_data()


def mean(data):
    return sum(data) / len(data)


average = mean(sample)
