#第一行為有N組測資
#每組測資兩行
#計算最大公因數
#利用輾轉相除法尋找最大公因數

n = int(input())
for i in range(n):
    s1 = int(input(), 2)
    s2 = int(input(), 2)
    while (s1 != 0):
        t = s1
        s1 = s2 % s1
        s2 = t
    if s2 != 1:
        print(f'Pair #{i+1}: All you need is love!')
    else:
        print(f'Pair #{i+1}: Love is not all you need!')
