def algorithm(n):
    c = 1
    while(n!=1):
        if(n%2==1):
            n = 3*n+1
        else:
            n /= 2
        c += 1
    return c

while True:
    try:
        i, j = map(int, input().split())
        if(i<=j):
            x = [algorithm(g) for g in range(i,j+1)]
        elif(j<i):
            x = [algorithm(g) for g in range(j,i+1)]
        print(f'{i} {j} {max(x)}')
    except ValueError:
        break

    