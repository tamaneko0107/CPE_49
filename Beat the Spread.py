#第一列為測資數量，每行測資有兩個值，分別是兩隊分數總合s，與兩隊分數差的絕對值d
#輸出兩隊的分數，分數大的在前，若沒有該值輸出impossible
#分數必定是大於等於0的整數

D = int(input())
for _ in range(D):
    s, d = map(int, input().split())
    if (d > s or (s-d) % 2 != 0):
        print("impossible")
    else:
        print(int((s+d)/2), end=" ")
        print(int((s-d)/2))
