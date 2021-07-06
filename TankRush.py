def TankRush(H1, W1, S1, H2, W2, S2):
    
    res = False
    
    for i in range(len(S1) - W1):
        
        count = i
        res = True
        
        for j in range(len(S2)):
            if S2[j] == ' ':
                count = count + W1 - j + 1
                continue
            if S1[count] == S2[j]:
                count += 1
            else:
                res = False
                break            
        
        if res: 
            return res
    
    return res