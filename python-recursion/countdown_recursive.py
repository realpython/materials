def countdown(n):
    print(n)
    if n == 0:
        return  # Terminate recursion
    else:
        countdown(n - 1)  # Recursive call


if __name__ == "__main__":
    countdown(5)
