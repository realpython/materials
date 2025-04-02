class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def give_raise(self, amount):
        self.salery = self.salary + amount  # Typo here: self.salery


john = Employee("John", "Engineering", 70000)
john.give_raise(5000)
print(john.salary)
print(john.__dict__)
