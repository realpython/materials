def cumulative_average():
    sample = []

    def average(new_value):
        sample.append(new_value)
        return sum(sample) / len(sample)

    return average


class CumulativeAverager:
    def __init__(self):
        self.sample = []

    def __call__(self, new_value):
        self.sample.append(new_value)
        return sum(self.sample) / len(self.sample)
