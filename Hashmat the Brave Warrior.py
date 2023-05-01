while True:
    try:
        x, y = map(int, input().split())
    except ValueError:
        break
    print(abs(x-y))
