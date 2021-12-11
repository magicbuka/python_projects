def move(A, i, j, left=False, right=False, down=False, up=False, ):
    if left: 
        A[i][j-1] = 0
    if right:
        A[i][j+1] = 0
    if down:
        A[i+1][j] = 0
    if up:
        A[i-1][j] = 0
    return A

def ConquestCampaign(N, M, L, battalion):
    days = 0
    A1 = [[1 for j in range(M)] for i in range(N)]
    A = [[1 for j in range(M)] for i in range(N)]
    
    for i in range(0, len(battalion), 2):
            a = battalion[i] - 1
            b = battalion[i+1] - 1
            A[a][b], A1[a][b]  = 0, 0
            
    days += 1
    
    while sum([sum(A1[i]) for i in range(N)])>0:
        
        rangeN = [*range(0, N)]
        rangeM = [*range(0, M)]
        
        for i in range(N):
            for j in range(M):
                if A1[i][j] == 0:
                    if i > min(rangeN) and i < max(rangeN) and j > min(rangeM) and j < max(rangeM):
                        move(A, i, j, left=True, right=True, down=True, up=True)
                    elif (i == min(rangeN) and j == min(rangeM)):
                        move(A, i, j, right=True, down=True)
                    elif (i == min(rangeN) and j == max(rangeM)):
                        move(A, i, j, left=True, down=True)
                    elif (i == max(rangeN) and j == min(rangeM)):
                        move(A, i, j, right=True, up=True)
                    elif (i == max(rangeN) and j == max(rangeM)):
                        move(A, i, j, left=True, up=True)
                    elif i == min(rangeN):
                        move(A, i, j, left=True, right=True, down=True)
                    elif i == max(rangeN): 
                        move(A, i, j, left=True, right=True, up=True)
                    elif j == min(rangeM): 
                        move(A, i, j, right=True, down=True, up=True)
                    elif j == max(rangeM):
                        move(A, i, j, left=True, down=True, up=True)
        
        A1 = A
        days += 1
    
    return days
