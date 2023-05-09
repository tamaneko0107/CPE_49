def square_len(r, c):
    up_limit = c
    down_limit = m-r-1
    left_limit = r
    right_limit = n-c-1
    limit = min(up_limit, down_limit, left_limit, right_limit)
    for i in range(limit, -1, -1):
        up_triangle = set(s[r-i][c-i:c+i+1]+s[r][c-i:c])
        down_triangle = set(s[r+i][c-i:c+i+1]+s[r][c+i:c])
        if up_triangle == down_triangle == set(s[r][c]):
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
