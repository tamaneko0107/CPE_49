#輸入第一行為測資數量
#每行包含一個數字N，為需要加密資料
#輸出加密後的b1與b2
#將N當作10進制轉成2進制，計算有b1個1
#將N當作16進位轉為2進制，計算有b2個1

t = int(input())
for i in range(t):
    n = input()
    x1 = bin(int(n))[2:]
    print(x1.count('1'), end=" ")
    x2 = bin(int(n, 16))[2:]
    print(x2.count('1'))
