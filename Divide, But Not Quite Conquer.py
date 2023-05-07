while True:
    try:
        n, m = map(int, input().split())
        a = [n]
        i = 0
        while a[-1] != 1 and m != 0:
            a.append(a[i]/m)
            i += 1
            if a[i] % m != 0:
                break
        if a[-1] == 1:
            for i in a:
                print(int(i), end=' ')
            print()
        else:
            print("Boring!")
    except EOFError:
        break
