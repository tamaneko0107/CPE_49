#公元年份非4的倍數，為平年。
#公元年份為4的倍數但非100的倍數，為閏年。
#公元年份為100的倍數但非400的倍數，為平年。
#公元年份為400的倍數為閏年。
data = [0,31,28,31,30,31,30,31,31,30,31,30,31]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
count = input()

for i in range(int(count)):
    M,D = input().split()
    sum = 4
    for i in range(int(M)):
        sum+=data[i]
    sum+=int(D)
    print(days[sum%7])
