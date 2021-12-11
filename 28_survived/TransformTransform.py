def Transform(A):
    B = []
    N = len(A)
    for i in range(0, N):
        for j in range(0, N-i):
            k = i + j
            sub_A = A[j:k+1]
            if sub_A:
                B.append(max(sub_A))
    return B

def TransformTransform(A, N):
    return not sum(Transform(Transform(A))) % 2
