toggle = True

for _ in range(4):
    if toggle:
        print(f"✅ toggle is {toggle}")
        print("Do something...")
    else:
        print(f"❌ toggle is {toggle}")
        print("Do something else...")
    toggle = not toggle
