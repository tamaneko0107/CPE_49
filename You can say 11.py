# 不可直接用%11判斷
#用奇數位和減去偶數位和再判斷是否可被11整除
#https://github.com/jlhung/UVA-Python/blob/master/10929%20-%20You%20can%20say%2011.py

while True:
    s = input()
    if s != '0':
        x = y = 0

        for i in range(0, len(s)):
            if i % 2 == 1:
                x += int(s[i])  #偶數位和
            else:
                y += int(s[i])  #奇數位和

        if abs(x-y) % 11 == 0:
            print("%s is a multiple of 11." % s)
        else:
            print("%s is not a multiple of 11." % s)

    else:
        break
