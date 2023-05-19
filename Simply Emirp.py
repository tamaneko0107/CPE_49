#每次測資有一個整數N
#判斷N整數和反轉後的N整數是否都是質數

def is_prime(n):
    for i in range(2, int(n**(1/2))+1, 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        n = input()
        n1 = int(n)
        n2 = int(n[::-1])
        if is_prime(n1):
            if n1 == n2 or not is_prime(n2):
                print(f'{n1} is prime.')
            else:
                print(f'{n1} is emirp.')
        else:
            print(f'{n1} is not prime.')

    except EOFError:
        break
