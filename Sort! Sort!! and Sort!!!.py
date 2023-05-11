#參考影片https://www.youtube.com/watch?v=533m4NjtVmQ

while True:
    n,m = map(int,input().split())
    print(n,m,sep=' ')
    if n == 0 and m == 0:
        break
    f=[]
    for i in range(n): f.append(int(input()))
    
    def cmp(x):
        pn = -1 if x<0 else 1
        k1 = abs(x)%m*pn
        if x&1: k2= -x
        else: k2 = x
        return k1,k2
    
    f.sort(key=cmp)
    print(*f,sep='\n')
