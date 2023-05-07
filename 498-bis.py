#參考影片https://www.youtube.com/watch?v=KtVFbcCfvkU

while True:
    try:
        x = int(input())
        a = list(map(int, input().split()))
        n = len(a)-1
        y = a[0]*n
        for i in range(1, n):
            y = y*x+a[i]*(n-i)
        print(y)
    except EOFError:
        break
