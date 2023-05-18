#參考影片
#https://www.youtube.com/watch?v=SFDhKo4tKDk
#(1-p^n)趨近於1
#用等比公式解題
#n玩家輪流擲骰子直到有玩家成功即停止
#需要輸出第i位玩家獲勝的機率，四捨五入到小數第四位
#輸入第一個整數唯有幾筆資料
#資料中包含N個玩家數，成功機率p，第i位玩家獲勝

data = int(input())

for _ in range(data):
    N, p, i = map(float, input().split())
    if p == 0:
        print('0.0000')
        continue
    pro = (pow(1-p,i-1)*p)/(1-pow(1-p,N))
    print(f'{pro:.04f}')