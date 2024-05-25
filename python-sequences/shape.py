class ShapePoints:
    """
    A ShapePoints object represents a collection of points

    Attributes:
    - points: sequence of points, where each point is a
        tuple (x, y)
    """

    def __init__(self, points):
        self.points = list(points)
        if points and self.points[0] != self.points[-1]:
            self.points.append(self.points[0])

    def __repr__(self):
        return f"ShapePoints({self.points})"

    def __getitem__(self, index):
        return self.points[index]

    def __len__(self):
        if self.points:
            return len(self.points) - 1
        return 0

    def __iter__(self):
        return iter(self.points)
