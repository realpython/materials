class Employee:
    count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")


jane = Employee("Jane Doe", "Software Engineer", 90000)
jane.display_profile()

john = Employee("John Doe", "Product Manager", 120000)
john.display_profile()

print(f"Total employees: {Employee.count}")
