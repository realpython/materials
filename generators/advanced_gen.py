import sys


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
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


def use_send():
    # Press Ctrl+C to stop the loop
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        pal_gen.send(10 ** (digits))


def use_throw():
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.send(10 ** (digits))


def use_close():
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.close()
        pal_gen.send(10 ** (digits))


def main():
    demos = {"send": use_send, "throw": use_throw, "close": use_close}
    choice = sys.argv[1] if len(sys.argv) > 1 else "close"
    demos[choice]()


if __name__ == "__main__":
    main()
