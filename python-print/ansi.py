def esc(*codes):
    return f"\033[{';'.join(str(code) for code in codes)}m"


print(esc(31, 1, 4) + "really" + esc(0) + " important")
