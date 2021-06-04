def squirrel(N):
    F = 1
    for i in range(2, N+1):
        F *= i
    return int(str(abs(F))[0])