while True:
    l = bin(int(input()))[2:]
    if l == '0':
        break
    print(f'The parity of {l} is {l.count("1")} (mod 2).')
