def print_four_members(member1, member2, /, member3, *, member4):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")
    print(f"member4 is {member4}")


print_four_members("Frank", "Dean", member3="Sammy", member4="Joey")
