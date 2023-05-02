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
        (lambda x: print(''.join(x)))(x)
    except EOFError:
        break
