from abc import ABC, abstractmethod

# Bad example
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height


# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("width", "height"):
#             self.__dict__["width"] = value
#             self.__dict__["height"] = value


# Good example
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2
