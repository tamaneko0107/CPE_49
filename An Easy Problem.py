#參考影片https://www.youtube.com/watch?v=4loEaRKBMlY
#一個R進制的數，如果是R-1的倍數，則其所有數字總和必為R-1的倍數
#輸入一個數N，推測該數的進制為多少
#輸入值可能帶有正負號開始或是空白，且有可能為0

def trans(s):
    if '0' <= s <= '9':
        return int(s)
    elif 'A' <= s <= 'Z':
        return ord(s)-ord('A')+10
    elif 'a' <= s <= 'z':
        return ord(s)-ord('a')+36

while True:
    try:
        number = input().strip(' +-')
        sum = 0
        r = trans(max(number))
        if r == 0:
            print("2")
            continue
        for i in number:
            sum += trans(i)
        for i in range(r,62):
            if sum % i == 0:
                print(i+1)
                break
            elif i == 61:
                print("such number is impossible!")
    except EOFError:
        break