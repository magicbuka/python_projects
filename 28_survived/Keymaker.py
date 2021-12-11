def Keymaker(k):
    if k == 1:
        return '1'
    
    line_doors = [0] * k
    for i in range(1, k+1):
        if i**2 <= k:
            line_doors[(i**2)-1] = 1
    
    return ''.join([str(x) for x in line_doors]) 
