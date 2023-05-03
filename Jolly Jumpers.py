def abs_data(x):
    y = []
    for i in range(len(x)-1):
        y.append(abs(x[i]-x[i+1]))
    return sorted(y)


while True:
    try:
        d = list(map(int, input().split()))
        jolly = abs_data(d)
        if set(range(1, max(jolly)+1)).issubset(jolly):
            print('Jolly')
        else:
            print('Not jolly')
    except EOFError:
        break
