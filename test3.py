# number = [1, 2, 3, 4, 4]
# print([i for i in range(len(number)) if number[i] == max(number)])

def n(x, y):
    for i in y:
        x[i] = 1
    return x


a = [6, 1, 3, 2, 2, 4, 8, 9, 12]  # 0,1,0,2,2,1,2


def cmp(x):
    pn = -1 if x < 0 else 1
    k1 = abs(x) % 3*pn
    if x & 1 == 0:
        k2 = -x
    else:
        k2 = x
    return k1, k2


print(sorted(a, key=cmp))
