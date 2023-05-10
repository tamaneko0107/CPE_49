while True:
    try:
        s = input()
        count = dict.fromkeys(map(ord, set(s)))
        for i in count:
            count[i] = s.count(chr(i))
        output = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        for i in output:
            print(i[0], i[1], sep=' ')
        print()
    except EOFError:
        break
