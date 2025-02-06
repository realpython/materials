from people_runtime import club, person


def main():
    p1 = person.Person("John", 30)
    p2 = person.Person("Jane", 29)
    c = club.Club("Tennis Club")
    c.assign_member(p1)
    c.assign_member(p2)
    print(c)


if __name__ == "__main__":
    main()
