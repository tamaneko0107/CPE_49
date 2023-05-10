field = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    map_list = []
    map_list.append('.'*m)
    for i in range(n):
        map_list.append('.'+input()+'.')
    map_list.append('.'*m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = 0
            if map_list[i][j] != '*':
                c += map_list[i-1][j-1:j+2].count('*')
                c += map_list[i][j-1:j+2].count('*')
                c += map_list[i+1][j-1:j+2].count('*')
                map_list[i] = map_list[i][:j]+str(c)+map_list[i][j+1:]
    print(f'Field #{field}:')
    for i in range(1, n+1):
        print(map_list[i][1:m+1])
    field += 1
