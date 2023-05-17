def cal(n):
    if (n >= 10000000):
        cal(n//10000000)
        print(" kuti", end="")
        n %= 10000000
    if (n >= 100000):
        cal(n//100000)
        print(" lakh", end="")
        n %= 100000
    if (n >= 1000):
        cal(n//1000)
        print(" hajar", end="")
        n %= 1000
    if (n >= 100):
        cal(n//100)
        print(" shata", end="")
        n %= 100
    if (n > 0):
        print(" "+str(n), end="")


cnt = 0
while True:
    cnt += 1
    try:
        s = int(input())
        print("{0:>4}.".format(cnt), end='')
        if (s != 0):
            cal(s)
        elif (s == 0):
            print(" 0", end='')
        print()
    except EOFError:
        break
