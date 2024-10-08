#判斷數入值N是否為9的倍數(每位數的總和為9的倍數)
#如果是，還要輸出深度(degree)
#N=0為結束

def degree(x, d=0):
    sum = 0
    d += 1
    for i in x:
        sum += int(i)
    if sum > 9:
        return degree(str(sum), d)
    elif sum == 9:
        return (True, d)
    elif sum < 9:
        return (False, d)


while True:
    i = input()
    if i == '0':
        break
    d = degree(i)
    if d[0]:
        print(f'{i} is a multiple of 9 and has 9-degree {d[1]}.')
    else:
        print(f'{i} is not a multiple of 9.')
