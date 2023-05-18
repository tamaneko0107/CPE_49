#判斷是否為B2數列
#B2數列條件為，下一個數皆比前一個數大，且每兩兩個數的總和皆不相等
#第一個數必須為>=1
#輸出與輸出間必須空一格

count = 1
while True:
    try:
        n = int(input())
        b = list(map(int, input().split()))
        non = input()
        s = set()
        not_B2 = 0
        if b[0] < 1:
            not_B2 = 1
        for i in range(n-1):
            if b[i+1] <= b[i] or not_B2 == 1:
                not_B2 = 1
                break
        for i in b:
            for j in b[b.index(i):]:
                if (i+j in s) or not_B2 == 1:
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
        print()
        count += 1
    except EOFError:
        break
