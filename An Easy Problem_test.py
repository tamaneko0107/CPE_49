#參考影片https://www.youtube.com/watch?v=4loEaRKBMlY
def trans(s):
    if '0' <= s <= '9':
        return int(s)
    elif 'A' <= s <= 'Z':
        return ord(s)-ord('A')+10
    elif 'a' <= s <= 'z':
        return ord(s)-ord('a')+36

while True:
    try:
        number = input()
        sum = 0
        r = trans(max(number))
        for i in number:
            sum += trans(i)
        for i in range(r,63):
            if sum % i == 0:
                print(i+1)
                break
            elif i == 62:
                print("such number is impossible!")
    except EOFError:
        break