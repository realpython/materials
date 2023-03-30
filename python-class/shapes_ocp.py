from abc import ABC, abstractmethod

# class Shape:
#     def __init__(self, shape_type, **kwargs):
#         self.shape_type = shape_type
#         if self.shape_type == "rectangle":
#             self.width = kwargs["width"]
#             self.height = kwargs["height"]
#         elif self.shape_type == "circle":
#             self.radius = kwargs["radius"]

#     def area(self):
#         if self.shape_type == "rectangle":
#             return self.width * self.height
#         elif self.shape_type == "circle":
#             return 3.14 * (self.radius**2)


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def area(self):
        return self.side**2
