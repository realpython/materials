class Record:
    """Hold a record of data."""


john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}


def as_dict(self):
    return self.__dict__


Record.as_dict = as_dict
print(Record.__dict__)

john_record = Record()
john_record.__dict__.update(john)
print(john_record.name)
print(john_record.department)
print(john_record.as_dict())
