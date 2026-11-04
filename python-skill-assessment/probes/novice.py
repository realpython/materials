cookies = 7
friends = 2

each = cookies // friends
left_over = cookies % friends

if left_over == 0:
    print(f"Everyone gets {each}, with none left over")
else:
    print(f"Everyone gets {each}, with {left_over} left over")

print(cookies / friends)
