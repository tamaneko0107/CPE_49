#公元年份非4的倍數，為平年。
#公元年份為4的倍數但非100的倍數，為閏年。
#公元年份為100的倍數但非400的倍數，為平年。
#公元年份為400的倍數為閏年。
#題目只求2011年

data = [0,31,28,31,30,31,30,31,31,30,31,30]  #12月的不需算入，不會超過2011年
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
count = input()

for i in range(int(count)):
    M,D = input().split()
    sum = 4   #2011年1月1日為星期六，從星期五的index開始計數
    for i in range(int(M)):
        sum+=data[i]
    sum+=int(D)
    print(days[sum%7])
