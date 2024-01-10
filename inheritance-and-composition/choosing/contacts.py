from representations import AsDictionaryMixin


class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2=""):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)


class _AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address("121 Admin Rd.", "Concord", "NH", "03301"),
            2: Address("67 Paperwork Ave", "Manchester", "NH", "03101"),
            3: Address("15 Rose St", "Concord", "NH", "03301", "Apt. B-1"),
            4: Address("39 Sole St.", "Concord", "NH", "03301"),
            5: Address("99 Mountain Rd.", "Concord", "NH", "03301"),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address


_address_book = _AddressBook()


def get_employee_address(employee_id):
    return _address_book.get_employee_address(employee_id)
