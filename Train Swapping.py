#泡沫排序法
#第一行資料代表有n筆測資
#每組測資第一行代表有多少節車廂
#需要將車廂順序依照1~L排序
#車廂每次只能移動一格
#輸出需要幾步驟

n = int(input())
for _ in range(n):
    l = int(input())
    train = list(map(int, input().split()))
    count = 0
    for i in range(l - 1):
        for j in range(l-1-i):
            if train[j] > train[j + 1]:
                temp = train[j+1]
                train[j + 1] = train[j]
                train[j] = temp
                count += 1
    print("Optimal train swapping takes %d swaps." % count)
