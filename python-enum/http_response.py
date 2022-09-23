from enum import IntEnum
from http.client import HTTPSConnection


class HTTPStatusCode(IntEnum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500


# def process_response(response):
#     match response.getcode():
#         case 200:
#             print("Success!")
#         case 201:
#             print("Successfully created!")
#         case 400:
#             print("Bad request")
#         case 404:
#             print("Not Found")
#         case 500:
#             print("Internal server error")
#         case _:
#             print("Unexpected status")


def process_response(response):
    match response.getcode():
        case HTTPStatusCode.OK:
            print("Success!")
        case HTTPStatusCode.CREATED:
            print("Successfully created!")
        case HTTPStatusCode.BAD_REQUEST:
            print("Bad request")
        case HTTPStatusCode.NOT_FOUND:
            print("Not Found")
        case HTTPStatusCode.SERVER_ERROR:
            print("Internal server error")
        case _:
            print("Unexpected status")


connection = HTTPSConnection("www.python.org")
try:
    connection.request("GET", "/")
    response = connection.getresponse()
    process_response(response)
finally:
    connection.close()
