# 使用公式解(一元二次方程式的)

import math
while True:
    try:
        S, D = map(int, input().split())
        print(math.ceil(((-1 + math.sqrt(1 - 4 * (-S*S + S - 2*D))) / 2)))
    except EOFError:
        break
