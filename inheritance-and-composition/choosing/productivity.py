class _ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError("role_id")
        return role_type()

    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")


class ManagerRole:
    def perform_duties(self, hours):
        return f"screams and yells for {hours} hours."


class SecretaryRole:
    def perform_duties(self, hours):
        return f"does paperwork for {hours} hours."


class SalesRole:
    def perform_duties(self, hours):
        return f"expends {hours} hours on the phone."


class FactoryRole:
    def perform_duties(self, hours):
        return f"manufactures gadgets for {hours} hours."


_productivity_system = _ProductivitySystem()


def get_role(role_id):
    return _productivity_system.get_role(role_id)


def track(employees, hours):
    _productivity_system.track(employees, hours)
