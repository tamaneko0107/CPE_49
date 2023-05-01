z = int(input())
total = []
for _ in range(z):
    country = input().split()[0]
    total.append(country)
for i in sorted(list(set(total))):
    print(f'{i} {total.count(i)}')
