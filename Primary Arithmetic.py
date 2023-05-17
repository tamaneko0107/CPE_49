while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    c, cnt = 0, 0  # c is carry, cnt is count
    while (x != 0 or y != 0):
        c = ((x % 10 + y % 10) + c)//10
        if c != 0:
            cnt += 1
        x //= 10
        y //= 10
    if cnt == 0:
        print("No carry operation.")
    elif cnt == 1:
        print("1 carry operation.")
    else:
        print(f'{cnt} carry operations.')
