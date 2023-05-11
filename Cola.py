#參考資料https://zerojudge.tw/ShowThread?postid=24624&reply=0
#可使用公式n*3/2取整數

while True:
    try:
        n = int(input())
        output = n
        while True:
            output += n//3
            if n < 3:
                break
            n = n//3+n % 3 #補充空瓶數
        if n == 2:
            output += 1    #還能再補充一瓶空瓶換一瓶
        print(output)
    except EOFError:
        break
