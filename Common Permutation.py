# 字母排序由小到大

while True:
    try:
        a = list(input())
        b = list(input())
        x = []

        for i in a:
            if (i in b):
                x.append(i)
                b.remove(i)
        x.sort()
        print(''.join(x))
    except EOFError:
        break
