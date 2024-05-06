from dataclasses import dataclass

# Point with slots
# class Point:
#     __slots__ = ("x", "y")

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# Regular class
# class ThreeDPoint:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __iter__(self):
#         yield from (self.x, self.y, self.z)

#     @classmethod
#     def from_sequence(cls, sequence):
#         return cls(*sequence)

#     @staticmethod
#     def show_intro_message(name):
#         print(f"Hey {name}! This is your 3D Point!")

#     def __repr__(self):
#         return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"


# Dataclass
@dataclass
class ThreeDPoint:
    x: int | float
    y: int | float
    z: int | float

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")
