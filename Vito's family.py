from sys import stdin

z = int(stdin.readline())
for _ in range(z):
    arr = [int(i) for i in stdin.readline().split()]
    mid = arr[0]//2
    arr = arr[1:]
    arr.sort()
    mid = arr[mid]
    result = [abs(mid-j) for j in arr]
    print(sum(result))