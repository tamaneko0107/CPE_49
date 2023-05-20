#參考影片https://youtu.be/03w6m8uYCqU
#1度=60分
#弧長為S = r*角度
#弦長 chord = 2*r*sin(a/2)
#輸入資料為三個整數，分別是地球表面到衛星的高度(s)，和角度(a)，最後是角度單位。
#r為6440
#輸出弧長與弦長

import math

while True:
    try:
        s,a,c = input().split()
        a = float(a)
        s = float(s)+6440
        if c == "min":
            a= a/60
        if a>180:
            a = 360-a
        rad = a*math.pi/180
        # print("{:.6f} {:.6f}".format(a*math.acos(-1)/180*s, 2*s*math.sin(a*math.acos(-1)/180/2)))
        print(f'{s*rad:.6f} {2*s*math.sin(rad/2):.6f}')
    except EOFError:
        break