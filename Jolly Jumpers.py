#題目為輸入n+1個整數，計算兩兩相鄰的絕對值差，如果絕對值差的序列存在1~n-1的計數則為jolly jumper，否則不是。
#輸入的第一個整數為n的值，也就是數列中有幾個整數

def abs_data(x):
    y = []
    for i in range(len(x)-1):
        y.append(abs(x[i]-x[i+1]))
    return y


while True:
    try:
        d = list(map(int, input().split()))
        jolly = abs_data(d[1:])
        if set(range(1, d[0])).issubset(jolly):
            print('Jolly')
        else:
            print('Not jolly')
    except EOFError:
        break
