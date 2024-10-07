from people import club, person


def main():
    p1 = person.Person("John", 30)
    p2 = person.Person("Jane", 29)
    c = club.Club("Tennis Club", [p1, p2])
    print(c)


if __name__ == "__main__":
    main()
