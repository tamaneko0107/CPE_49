#第一行為指令個數
#指令為朝哪個方向滾

while True:
    n = int(input())
    if n == 0:
        break
    x = [1, 4, 6, 3]    #[上，東，下，西]
    y = [1, 2, 6, 5]    #[上，北，下，南]
    for i in range(n):
        command = input()
        if command == 'north':
            temp = y.pop()
            y.insert(0, temp)
        if command == 'south':
            temp = y.pop(0)
            y.append(temp)
            temp = y[0]
        if command == 'east':
            temp = x.pop()
            x.insert(0, temp)
        if command == 'west':
            temp = x.pop(0)
            x.append(temp)
            temp = x[0]
        x[0] = temp
        x[2] = 7-temp
        y[0] = temp
        y[2] = 7-temp
    print(x[0])
