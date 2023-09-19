def print_varying_members(member1, member2, *args, member3):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")
    print(f"*args contains {args}")


print_varying_members("Frank", member2="Dean", member3="Sammy")
print_varying_members(member1="Frank", member2="Dean", member3="Sammy")
print_varying_members("Frank", "Dean", "Peter", "Joey", member3="Sammy")

# This would be invalid:
# print_varying_members(member1="Frank", "Dean", member3="Sammy")
