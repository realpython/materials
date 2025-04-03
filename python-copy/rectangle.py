import copy


class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f"Rectangle({self.top_left}, {self.bottom_right})"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


if __name__ == "__main__":
    bounding_box = Rectangle(
        top_left := Point(10, 20), bottom_right := Point(30, 40)
    )
    shallow_copy = copy.copy(bounding_box)
    deep_copy = copy.deepcopy(bounding_box)

    bounding_box.bottom_right = Point(500, 700)
    bottom_right.x += 100

    print(f"{bounding_box = }")
    print(f"{shallow_copy = }")
    print(f"{deep_copy = }")
