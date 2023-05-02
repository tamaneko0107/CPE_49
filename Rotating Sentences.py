slist = []
while True:
    try:
        slist.append(input())
    except EOFError:
        break

slist = slist[::-1]
col = len(slist)
row = 0
for i in slist:
    row = max(row, len(i))
for i in range(row):
    for j in range(col):
        if i < len(slist[j]):
            print(slist[j][i], end='')
        else:
            print(' ', end='')
    print()
