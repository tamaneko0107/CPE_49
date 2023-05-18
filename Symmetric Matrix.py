#檢查該N*N的矩陣是否為對稱中心點的矩陣
#將矩陣攤平成一列可發現左右相反對稱

def is_symmetric(matrix, n):
    index = 0
    while (index <= (n*n-1-index)):
        if (matrix[index] != matrix[n*n-1-index]) or (matrix[index] < 0):
            return False
        index += 1
    return True


T = int(input())
for i in range(T):
    N = int(input()[4::])
    M = []
    for _ in range(N):
        M.extend(list((map(int, input().split()))))
    if is_symmetric(M, N):
        print(f'Test #{i+1}: Symmetric.')
    else:
        print(f'Test #{i+1}: Non-symmetric.')
