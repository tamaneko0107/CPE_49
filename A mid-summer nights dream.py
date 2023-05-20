#參考影片https://www.youtube.com/watch?v=lSh7iT8cnYk
#輸入第一行代表有n組測資
#找出一組測資中的中位數(A)與測資中有幾項符合要求，最後還有總共有多少總可能

while True:
    try:
        n = int(input())
        x = []
        for i in range(n):
            x.append(int(input()))
        x = sorted(x)
        if n%2==1:
            min = x[n//2]
            max = x[n//2]
        else:
            min = x[n//2-1]
            max = x[n//2]
        count = 0
        for i in x:
            if i==min or i==max:
                count+=1
            elif i>max:
                break
        possible = max-min+1
        print("%d %d %d" % (min,count,possible))
    except EOFError:
        break
        