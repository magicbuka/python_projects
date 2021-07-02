def Unmanned(L, N, track):
    t = 0
    position = 1
    j = 0    
    for i in range(position, L+1, 1):
        t += 1
        if j < N and i == track[j][0]:
            position = i + 1
            per = 0
            while per < t:
                for d in range(1,3,1):       
                    per += track[j][d]
                    if per >= t: break 
            if d == 1: t += per - t
            j += 1
    return t