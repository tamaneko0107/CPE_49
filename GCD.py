#每行有一個測資N，計算該值的GCD(i,j)
#每一個N的G與N-1的G都差(i,N) for i in range(1,N)

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
        for i in range(list_max+1, n+1):
            for j in range(1, i):
                g += gcd(j, i)
            gcd_list[i] = g
    print(gcd_list[n])
