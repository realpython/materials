# from people_runtime.club import Club


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clubs = set()

    def __str__(self):
        return f"{self.name} ({self.age})"

    def join_club(self, club):
        from people_runtime.club import Club

        if isinstance(club, Club):
            self.clubs.add(club)
            if self not in club.members:
                club.assign_member(self)
        else:
            raise ValueError("Can only join instances of Club")
