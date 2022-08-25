class LowerString(str):
    def __init__(self, string):
        super().__init__(string.lower())


# class LowerString(str):
#     def __new__(cls, string):
#         instance = super().__new__(cls, string.lower())
#         return instance

# from collections import UserString


# class LowerString(UserString):
#     def __init__(self, string):
#         super().__init__(string.lower())
