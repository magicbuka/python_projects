def MatrixTurn(Matrix, M, N, T):
    
    matrix = [[None for i in range(N)] for _ in range(M)]
    
    for t in range(T):
        k = 0
        l = 0
        count = 0
        while count < N*M:
            for i in range(k, M-k):
                for j in range(l, N-l):
                    if (i == k or i not in (k, M-k-1)) and j == l:
                        matrix[i][j] = Matrix[i+1][j]
                        count += 1
                    elif i == k and j > l:
                        matrix[i][j] = Matrix[i][j-1]
                        count += 1
                    elif (i not in (k, M-k-1) or i == M-k-1) and j == N-l-1:
                        matrix[i][j] = Matrix[i-1][j]
                        count += 1 
                    elif i == M-k-1 and j < N-l-1:
                        matrix[i][j] = Matrix[i][j+1]
                        count += 1
            k += 1
            l += 1
        
        for i in range(M):
            Matrix[i] = ''.join(matrix[i])
