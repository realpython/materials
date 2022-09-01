class WordCountString(str):
    def words(self, separator=None):
        return len(self.split(separator))


# from collections import UserString


# class WordCountString(UserString):
#     def words(self, separator=None):
#         return len(self.split(separator))
