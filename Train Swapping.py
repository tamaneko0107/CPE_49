#泡沫排序法

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
