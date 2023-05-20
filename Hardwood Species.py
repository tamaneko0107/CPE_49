#參考資料https://vgoin.citypro.tw/CT/REItem.aspx?p=A1006044-CT2346
#計算每種數占的比率
#按照樹種字母排序
import sys

n = int(input())
start = input()

for i in range(n):
    data = {}
    total = 0
    for line in sys.stdin:
        species = line.strip()
        if species:
            data[species] = data.get(species, 0) + 1
            total += 1
        else:
            break
    for j in sorted(data.keys()):
        print(f'{j} {data[j]/total*100:.4f}')
    if i != n-1:
        print()
