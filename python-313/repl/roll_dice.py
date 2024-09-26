import random

num_faces = 6

print("Hit enter to roll die (q to quit, number for # of faces) ")
while True:
    roll = input()
    if roll.lower().startswith("q"):
        break
    if roll.isnumeric():
        num_faces = int(roll)

    result = random.randint(1, num_faces)
    print(f"Rolling a d{num_faces:<2d} -  {result:2d}")
