D = int(input())
for _ in range(D):
    s, d = map(int, input().split())
    if (d > s or (s-d) % 2 != 0):
        print("impossible")
    else:
        print(int((s+d)/2), end=" ")
        print(int((s-d)/2))
