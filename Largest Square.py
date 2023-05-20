#第一組測資代表有T組資料
#接著有三個數M,N,Q，M、N分別代表矩陣的高度與寬度，Q代表詢問的數量
#每個詢問值包含兩個整數r,c
#輸出以(r,c)為中心點的最大正方形邊長

def square_len(r, c):
    up_limit = r   #r
    down_limit = m-r-1
    left_limit = c
    right_limit = n-c-1
    limit = min(up_limit, down_limit, left_limit, right_limit)
    for i in range(limit, -1, -1):
        check = set(map(lambda x: ''.join(set(x[c-i:c+i+1])), s[r-i:r+i+1]))
        if check == set(s[r][c]):
            return 2*i+1


t = int(input())
for _ in range(t):
    m, n, q = map(int, input().split())
    print(m, n, q, sep=' ')
    s = []
    for i in range(m):
        s.append(input())
    for i in range(q):
        r, c = map(int, input().split())
        print(square_len(r, c))
