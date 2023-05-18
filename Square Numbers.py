#計算一個值域內有多少個完全平方數

while True:
    a, b = map(lambda x: int(x)**(1/2), input().split())
    if a == 0 and b == 0:
        break
    if a-int(a) == 0:
        print(int(b)-int(a)+1)
    else:
        print(int(b)-int(a))
