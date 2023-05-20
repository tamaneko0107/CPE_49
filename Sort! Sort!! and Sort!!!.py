#參考影片https://www.youtube.com/watch?v=533m4NjtVmQ
#第一行有兩個整數N、M，接著有N個整數
#依據每個數字除以M的餘數由小到大排，若排序中比較的兩數為一奇一偶且兩數除以M 的餘數相等，則奇數要排在偶數前面。
#若兩奇數除以M餘數大小相等，則原本數值較大的奇數排在前面。
#同樣的，若兩偶數除以M餘數大小相等，則較小的偶數排在前面。
#至於負數的餘數計算和 C 語言裡的定義相同，即負數的餘數絕對不會大於零。

while True:
    n,m = map(int,input().split())
    print(n,m,sep=' ')
    if n == 0 and m == 0:
        break
    f=[]
    for i in range(n): f.append(int(input()))
    
    def cmp(x):
        pn = -1 if x<0 else 1
        k1 = abs(x)%m*pn
        k2 = x%2==0
        if x&1:
            k3 = -x
        else:
            k3 = x
        return k1,k2,k3
    
    f.sort(key=cmp)
    print(*f,sep='\n')
