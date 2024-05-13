import os
import unittest
from tempfile import NamedTemporaryFile

from employee import from_csv_file

SAMPLE_CSV = """name,age,job,salary
Alice,25,Engineer,50000
Bob,30,Analyst,60000
Jane,35,Manager,80000
John,40,CEO,100000
"""


class TestFromCsvFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_file = NamedTemporaryFile(
            delete=False,
            mode="w",
            newline="",
            suffix=".csv",
        )
        cls.temp_file_name = cls.temp_file.name
        cls.temp_file.write(SAMPLE_CSV)
        cls.temp_file.close()
        cls.employees = from_csv_file(cls.temp_file_name)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.temp_file_name)

    def test_from_csv_file_total_employees(self):
        self.assertEqual(len(self.employees), 4)

    def test_from_csv_file_employee_attributes(self):
        self.assertEqual(self.employees[0].name, "Alice")
        self.assertEqual(self.employees[0].age, 25)
        self.assertEqual(self.employees[0].job, "Engineer")
        self.assertEqual(self.employees[0].salary, 50000.0)

    def test_from_csv_file_employee_name(self):
        self.assertEqual(self.employees[0].name, "Alice")
        self.assertEqual(self.employees[1].name, "Bob")
        self.assertEqual(self.employees[2].name, "Jane")
        self.assertEqual(self.employees[3].name, "John")


if __name__ == "__main__":
    unittest.main(verbosity=2)
