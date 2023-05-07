t = int(input())
for i in range(t):
    n = input()
    x1 = bin(int(n))[2:]
    print(x1.count('1'), end=" ")
    x2 = bin(int(n, 16))[2:]
    print(x2.count('1'))
