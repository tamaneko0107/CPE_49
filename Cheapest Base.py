#參考影片https://youtu.be/z8cM3pTXqUI

def base_change(n,data):
    output=[]
    for base in range(2,37):
        ans = []
        temp = n
        while temp:
            ans.append(temp%base)
            temp //= base
        total = 0
        for i in ans:
            total+=data[i]
        output.append(total)
    return output

    #進制轉換與cost總和
    # total = [0 for i in range(35)]
	# 	for k in range(2, 37):
	# 		t = number
	# 		while t > 0:
	# 			total[k-2] += a[t % k]
	# 			t //= k
    

case = int(input())

for i in range(case):
    print(f'Case {i+1}:')
    
    data = []
    for _ in range(4):
        data.extend(map(int,input().split()))
    
    input_data = int(input())
    for j in range(input_data):
        d = int(input())
        base_data = base_change(d,data)
        min_cost = min(base_data)
        print(f'Cheapest base(s) for number {d}:',end='')
        for x,y in enumerate(base_data):
            if y == min_cost:
                print(f' {x+2}',end='')
        print()
    if i != case-1:
        print()
