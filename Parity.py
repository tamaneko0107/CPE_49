#對一個數入值，求該值的同位元(計算二進制1的個數即可)

while True:
    l = bin(int(input()))[2:]
    if l == '0':
        break
    print(f'The parity of {l} is {l.count("1")} (mod 2).')
