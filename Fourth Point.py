#參考資料https://fg123789hj.pixnet.net/blog/post/282391784
#利用平行四邊形座標相加特性

while True:
    try:
        point = list(map(float,input().split()))
        x = point[0::2]
        y = point[1::2]
        x_endpoint = sum(x)
        y_endpoint = sum(y)
        stop = 0
        for i in range(4):
            for j in range(i+1,4):
                if x[i] == x[j] and y[i] == y[j]:
                    x_endpoint-=x[i]*3
                    y_endpoint-=y[i]*3
                    print(f'{x_endpoint:.3f} {y_endpoint:.3f}')
                    stop = 1
                    break
            if stop == 1:
                break
    except EOFError:
        break