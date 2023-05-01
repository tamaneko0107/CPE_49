z = int(input())
total = {}
for _ in range(z):
    word = input().upper()
    for i in word:
        if ('A' <= i and i <= 'Z'):
            total.setdefault(i, 0)
            total[i] += 1
total = sorted(total.items(), key=lambda i: (-i[1], i[0]))
for i in total:
    print(f'{i[0]} {i[1]}')
