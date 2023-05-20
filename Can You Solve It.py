#參考資料https://fg123789hj.pixnet.net/blog/post/282321356
#利用等差，上底(x2+y2)加下底(x1+y1+1)乘高(x2+y2-x1-y1)除2
#最後加上高度差
#第一行為有幾組測資
#接著有四個整數分別代表起始點(x1,y1)和目標點(x2,y2)
#輸出需要幾步

n = int(input())
for i in range(n):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    count += (x1+y1+x2+y2+1)*(x2+y2-x1-y1)/2
    count += x2-x1  #高度修正
    print(f'Case {i+1}: {int(count)}')
