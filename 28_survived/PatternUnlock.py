def PatternUnlock(N, hits): 
    
    dd = 2**0.5
    d = {1:1, 3:1, 4:[1, dd], 6:1, 8:1, 2:dd, 5:[1, dd], 7:dd}
    
    num_res = 0
    for i in range(N-1):
        check = abs(hits[i] - hits[i+1])
        if (check == 4 and hits[i] in [3, 7]) or (check == 5 and hits[i] in [6, 1]):
            num_res += d[check][0]
        elif (check == 4 and hits[i] not in [3, 7]) or (check == 5 and hits[i] not in [6, 1]):
            num_res += d[check][1]
        else:
            num_res += d[check]
            
    result = ''
    for num in str(int(round(num_res, 5)*100000)):
        if num != '0':
            result += num
        
    return result
