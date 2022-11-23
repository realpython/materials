from enum import Enum, unique

# class OperatingSystem(Enum):
#     UBUNTU = "linux"
#     MACOS = "darwin"
#     WINDOWS = "win"
#     DEBIAN = "linux"


@unique
class OperatingSystem(Enum):
    UBUNTU = "linux"
    MACOS = "darwin"
    WINDOWS = "win"
    DEBIAN = "linux"
