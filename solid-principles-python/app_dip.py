from abc import ABC, abstractmethod

# Bad example
# class FrontEnd:
#     def __init__(self, back_end):
#         self.back_end = back_end

#     def display_data(self):
#         data = self.back_end.get_data_from_database()
#         print("Display data:", data)


# class BackEnd:
#     def get_data_from_database(self):
#         """Return data from the database."""
#         return "Data from the database"


# Good example
class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
