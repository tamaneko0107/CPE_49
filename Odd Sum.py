T = int(input())
for i in range(T):
    a = int(input())
    b = int(input())

    if (a % 2 == 1):
        total = sum(list(range(a, b+1, 2)))
    else:
        total = sum(list(range(a+1, b+1, 2)))

    print(f'Case {i+1}: {total}')
