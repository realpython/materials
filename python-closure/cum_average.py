def cumulative_average():
    data = []

    def average(value):
        data.append(value)
        return sum(data) / len(data)

    return average
