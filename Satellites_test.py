#參考影片https://youtu.be/03w6m8uYCqU
#1度=60分
#弧長為S = r*角度
#弦長 chord = 2*r*sin(a/2)

import math

while True:
    try:
        s,a,c = input().split()
        a = float(a)
        s = float(s)
        if c == "min":
            a= a/60
        if a>180:
            a = 360-a
        rad = a*math.pi/180
        print(round((s+6440)*rad,6),end=" ")
        print(round(2*(s+6440)*math.sin(rad/2),6))
    except EOFError:
        break