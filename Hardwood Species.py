#參考資料https://vgoin.citypro.tw/CT/REItem.aspx?p=A1006044-CT2346

n = int(input())
start = input()

for i in range(n):
    data = {}
    total = 0
    while True:
        try:
            tree = input()
            if tree == start:
                break
            data.setdefault(tree, 0)
            data[tree] += 1
            total += 1
        except EOFError:
            break
    for i in sorted(data.keys()):
        print(f'{i} {data[i]/total*100:.4f}')
    print()
