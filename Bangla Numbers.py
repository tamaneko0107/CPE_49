m = [100, 10, 100, 100, 100]
q = ["", "shata", "hajar", "lakh", "kuti"]

cnt = 0
while True:
    cnt+=1
    try:
        s = int(input())
        temp = s
        p = []
        cont = 0
        result = ""

        while(temp!=0):
            temp//=1000000000
            cont+=1

        if(cont==0):
            print(f'{cnt}. 0')
        else:
            for i in range(cont):
                for j in range(0,4):
                    p.append(s%m[j])
                    s//=m[j]
                p.append(s%m[4])
                s-=s%m[4]

            for i in range(len(p)//5):
                for j in range(4, -1, -1):
                    pp = p.pop()
                    if(pp!=0):
                        result += str(pp)+" "+q[j]+" "
            print(f'{cnt}. {result[:-2]}')
    except ValueError:break