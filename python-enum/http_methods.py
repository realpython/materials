import enum

# HTTPMethod = enum.Enum(
#     "HTTPMethod", ["GET", "POST", "PUSH", "PATCH", "DELETE"]
# )


class HTTPMethod(enum.Enum):
    GET = 1
    POST = 2
    PUSH = 3
    PATCH = 4
    DELETE = 5
