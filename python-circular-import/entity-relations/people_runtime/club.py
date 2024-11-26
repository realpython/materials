# from people_runtime.person import Person


class Club:
    def __init__(self, name):
        self.name = name
        self.members = set()

    def __str__(self):
        return f"{self.name} ({len(self.members)} members)"

    def assign_member(self, person):
        from people_runtime.person import Person

        if isinstance(person, Person):
            self.members.add(person)

            if self not in person.clubs:
                person.join_club(self)
        else:
            raise ValueError("Can only assign instances of Person")
