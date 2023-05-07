t = int(input())
for _ in range(t):
    n = int(input())
    p = int(input())
    hi = []
    for _ in range(p):
        i = int(input())
        hi.extend(list(range(i-1, n, i)))
    lost = 0
    for i in set(hi):
        if i % 7 != 5 and i % 7 != 6:
            lost += 1
    print(lost)
