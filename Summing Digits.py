from functools import reduce


def f(n):
    if (len(n) == 1):
        print(int(n))
    else:
        l = map(int, n)
        r = reduce(lambda x, y: x+y, list(l))
        return f(str(r))


while True:
    try:
        s = input()
        if (s == "0"):
            break
        else:
            f(s)
    except ValueError:
        break
