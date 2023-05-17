#參考資料https://github.com/jlhung/UVA-Python/blob/master/100%20-%20The%203n%20%2B%201%20problem.py

def algorithm(n):
    if n in d:
        return d[n]
    if n <= 1:
        return 1
    if n % 2 == 1:
        y = 3*n+1
    else:
        y = n//2
    d[n] = 1 + algorithm(y)
    return d[n]


d = {}
while True:
    try:
        x, y = map(int, input().split())
        max_cy = 0
        for i in range(min(x, y), max(x, y)+1):
            n = algorithm(i)
            if n > max_cy:
                max_cy = n
        print(f'{x} {y} {max_cy}')
    except EOFError:
        break
