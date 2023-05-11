def cumulative_average():
    data = []

    def average(new_value):
        data.append(new_value)
        return sum(data) / len(data)

    return average


class CumulativeAverager:
    def __init__(self):
        self.data = []

    def __call__(self, new_value):
        self.data.append(new_value)
        return sum(self.data) / len(self.data)
