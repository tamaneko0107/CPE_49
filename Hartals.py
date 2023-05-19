#輸入第一行為T組測資
#每組測資第一行包含一個整數N代表模擬的天數
#接著下一行代表有P個政黨
#接著有P行的資料分別代表第i個政黨的霸會參數(每幾天霸會一次)
#每次模擬都從星期天開始，星期五和六不進行霸會
#輸出會因霸會損失多少工作日(在星期五、六)

t = int(input())
for _ in range(t):
    n = int(input())
    p = int(input())
    hi = []
    for _ in range(p):
        i = int(input())
        hi.extend(list(range(i-1, n, i)))  #霸會參數即為從星期幾開始霸會，並每i天進行一次
    lost = 0
    for i in set(hi):
        if i % 7 != 5 and i % 7 != 6:
            lost += 1
    print(lost)
