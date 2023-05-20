#給一列文字計算各字元的出現次數
#排序方式依照出現次數由低到高，若相同則ASCII較大的排前面

n = 0
while True:
    try:
        s = input()
        count = dict.fromkeys(map(ord, set(s)))
        for i in count:
            count[i] = s.count(chr(i))
        output = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        if n == 1:
            print()
        for i in output:
            print(i[0], i[1], sep=' ')
        n = 1
    except EOFError:
        break
