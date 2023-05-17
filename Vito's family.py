z = int(input())
for _ in range(z):
    arr = list(map(int, input().split()))
    mid = arr[0]//2
    arr = arr[1:]
    arr.sort()
    mid = arr[mid]
    result = [abs(mid-j) for j in arr]
    print(sum(result))
