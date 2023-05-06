count = 1
while True:
    try:
        n = int(input())
        b = list(map(int, input().split()))
        s = set()
        not_B2 = 0
        for i in b:
            for j in b[b.index(i):]:
                if i+j in s:
                    not_B2 = 1
                    break
                else:
                    s.add(i+j)
            if not_B2 == 1:
                break
        if not_B2 == 1:
            print(f'Case #{count}: It is not a B2-Sequence.')
        else:
            print(f'Case #{count}: It is a B2-Sequence.')
        count += 1
    except EOFError:
        break
