def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    if num == reversed_num:
        return num
    else:
        return False


# Press Ctrl+C to stop the loop
for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        print(i)
