def gcd(a, b):
    if a:
        return gcd(b % a, a)
    else:
        return b


gcd_list = {2: 1}
while True:
    n = int(input())
    if n == 0:
        break
    list_max = list(gcd_list.keys())[-1]
    if list_max < n:
        g = gcd_list[list_max]
        for i in range(list_max, n):
            for j in range(1, i+1):
                g += gcd(j, i+1)
            gcd_list[i+1] = g
    print(gcd_list[n])
