def PatternUnlock(N, hits): 
    
    dd = 2**(1/2)
    d = {1:1, 3:1, 4:[1, dd], 6:1, 8:1, 2:dd, 5:dd, 7:dd}
    
    num_res = 0
    for i in range(N-1):
        check = abs(hits[i] - hits[i+1])
        if check == 4:
            if hits[i] in [6, 1, 3, 7]:
                num_res += d[check][1]
            else:
                num_res += d[check][0]
        else:
            num_res += d[check]
            
    result = ''
    for num in str(int(round(num_res, 5)*100000)):
        if num != '0':
            result += num
        
    return result