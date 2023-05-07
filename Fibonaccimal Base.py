def fib_base(n):
    s = ""
    i = 1
    fib_list = [0, 1]
    while True:
        if fib_list[i] <= n:
            i += 1
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        else:
            break
    for j in range(i-1, 1, -1):
        if n >= fib_list[j]:
            s += '1'
            n -= fib_list[j]
        else:
            s += '0'
    return s


n = int(input())
for i in range(n):
    x = int(input())
    print(f'{x} = {fib_base(x)} (fib)')
