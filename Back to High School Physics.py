# 圖形會是一個梯形(v-t)，其中v為梯形的中線，梯形高度為2t
# 梯形面積代表位移距離，可用梯形中線長*梯形高度來計算

while True:
    try:
        v,t = map(int, input().split())
        print(2*t*v)
    except EOFError:
        break