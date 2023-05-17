i = "234567890-=ertyuiop[]\\dfghjkl;'cvbnm,./"
o = "`1234567890qwertyuiop[asdfghjklzxcvbnm,"

while True:
    try:
        s = input()
    except EOFError:
        break

    trans = s.maketrans(i, o)
    print(s.translate(trans))
