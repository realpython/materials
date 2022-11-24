from enum import Enum

# HTTPMethod = Enum(
#     "HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"]
# )


class HTTPMethod(Enum):
    GET = 1
    POST = 2
    PUSH = 3
    PATCH = 4
    DELETE = 5
