def MisterRobot(N,data):
    res = -1
    
    while res == -1:
        res = 1
        for i in range(N-1):
            if data[i] > data[i+1]:
                res = 0
                if i != N-2:
                    lst = data[i:i+2] 
                    lst.insert(0, lst.pop())
                    data[i:i+2] = lst
                    res = -1    
                    break
                
        if res == 1:
            return True
        elif res == 0:
            return False