def MadMax(N, Tele):
    
    Tele.sort()
    min_t, max_t, median_ind = min(Tele), max(Tele), (len(Tele)//2) 
    left, right = Tele[0:median_ind], Tele[median_ind:]
    right.sort(reverse=True)
    
    return left + right
