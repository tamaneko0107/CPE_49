while True:
    s = int(input())
    if s!=0:
        if(s%11==0):
            print("{} is a multiple of 11.".format(s))
        else:
            print("{} is not a multiple of 11.".format(s))
    else:
        break