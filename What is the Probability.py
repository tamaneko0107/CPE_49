#參考影片
#https://www.youtube.com/watch?v=SFDhKo4tKDk
#(1-p^n)趨近於1

data = int(input())

for i in range(data):
    N, p, i = map(float, input().split())
    pro = (pow(1-p,i-1)*p)/(1-pow(1-p,N))
    print(round(pro,4))