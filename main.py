import string

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(len(CHARS))


def baseChanger(num, fromBase, toBase) -> string:
    return base10ToNewBase(oldBaseTo10Base(num, fromBase), toBase)


def base10ToNewBase(num, base) -> string:
    final = ""
    num = int(num)
    base = int(base)
    while 1:

        final = str(CHARS[num % base]) + final
        num = num // base

        if num == 0:
            return final


def oldBaseTo10Base(num, base) -> string:
    num = str(num)
    base = int(base)
    num = num[::-1]

    final = 0
    for i in range(0, len(num)):
        final += int(CHARS.find(num[i])) * base ** i

    return final


# Change Base from 10 to 2
print(baseChanger("5", 10, 2))  # result -> "101"

# Change Base from 2 to 10
print(baseChanger("101", 2, 10))  # result -> "5"

# Change Base from 10 to 16
print(baseChanger("123456", 10, 16))  # result -> "1E240"

# Change Base from 16 to 10
print(baseChanger("1E240", 16, 10))  # result -> "123456"
