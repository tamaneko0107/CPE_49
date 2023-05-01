directions = {
    # direction: (x, y)
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1),
}
d = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
max_x, max_y = map(int, input().split())
LOST = set()
while True:
    try:
        s = input().split()
        currentX, currentY = map(int, s[:2])
        direct = s[2]
        cur_dir = d[direct]
        l = 0

        for c in input():
            l = 0
            if c == 'L':
                cur_dir = (cur_dir + 3) % 4
            elif c == 'R':
                cur_dir = (cur_dir + 1) % 4
            elif c == 'F':
                moveX, moveY = directions[cur_dir]

                if (currentX + moveX < 0 or currentX + moveX > max_x
                            or currentY + moveY < 0 or currentY + moveY > max_y
                        ):
                    if (currentX, currentY) in LOST:
                        continue

                    l = 1
                    print(currentX, currentY, list(d.keys())[cur_dir], 'LOST')
                    LOST.add((currentX, currentY))
                    break
                else:
                    currentX += moveX
                    currentY += moveY
        if l != 1:
            print(currentX, currentY, list(d.keys())[cur_dir])

    except EOFError:
        break
