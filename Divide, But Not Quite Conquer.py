# 1. a[1] = n, a[i] = a[i − 1] ÷ m, for all 1 < i ≤ k
# 2. a[i] 被 m 整除(a[i] mod m = 0) for all 1 ≤ i < k
# 3. a[1] > a[2] > a[3] > ... > a[k]
#每次輸入有兩個數n,m，兩數均有可能為0和1
#必須符合上述條件才能，否則輸出Boring!
#輸出a數列

while True:
    try:
        n, m = map(int, input().split())
        a = [n]
        if m <= 1 or n <= 1:
            print("Boring!")
            continue
        while a[-1]%m == 0:
            a.append(a[-1]/m)
        if a[-1] == 1:
            print(*map(int,a))
        else:
            print("Boring!")
    except EOFError:
        break
