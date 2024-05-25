from contacts import get_employee_address
from hr import get_policy
from productivity import get_role
from representations import AsDictionaryMixin


class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {"name": "Mary Poppins", "role": "manager"},
            2: {"name": "John Smith", "role": "secretary"},
            3: {"name": "Kevin Bacon", "role": "sales"},
            4: {"name": "Jane Doe", "role": "factory"},
            5: {"name": "Robin Williams", "role": "secretary"},
        }

    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info


class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get("name")
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get("role"))
        self._payroll = get_policy(self.id)

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()
