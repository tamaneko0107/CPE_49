#參考資料https://fg123789hj.pixnet.net/blog/post/282321356
#利用等差，上底(x2+y2)加下底(x1+y1+1)乘高(x2+y2-x1-y1)除二
#最後加上高度差

n = int(input())
for i in range(n):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    count += (x1+y1+x2+y2+1)*(x2+y2-x1-y1)/2
    count += x2-x1
    print(f'Case {i+1}: {int(count)}')
