# 使用公式解(一元二次方程式的)
#S+(S+1)+(S+2)+...+n <= D
#有n個旅客的旅行團會在飯店停留n天
#每次入住的旅行團都會比前一次多1人(n+1)
#求第D天入住的旅行團人數
#輸入有兩筆資料，第一組旅行團的人數S，查詢第D天入住的旅行團人數

import math
while True:
    try:
        S, D = map(int, input().split())
        print(math.ceil(((-1 + math.sqrt(1 - 4 * (-S*S + S - 2*D))) / 2)))
    except EOFError:
        break
